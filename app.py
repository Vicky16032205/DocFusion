import os
import streamlit as st
import subprocess
import sys

from pymilvus import MilvusClient


if os.name == "nt":  # Windows
    VENV_PYTHON = os.path.join(sys.prefix, "Scripts", "python.exe")
else:  # Linux/macOS
    VENV_PYTHON = os.path.join(sys.prefix, "bin", "python")

# Milvus Client Setup - Initialize on demand
@st.cache_resource
def get_milvus_client():
    try:
        return MilvusClient(
            uri="http://localhost:19530",
            token="root:Milvus"
        )
    except Exception as e:
        st.error(f"Failed to connect to Milvus: {e}")
        return None

# def run_command(command):
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                 text=True, bufsize=1, encoding="utf-8", errors="replace")
    
#     output_area = st.empty()  # Placeholder for live output
#     error_area = st.empty()   # Placeholder for errors
    
#     output_text = []
#     error_text = []

#     for line in process.stdout:
#         output_text.append(line)
#         output_area.text_area("Processing Output", "".join(output_text), height=300)

#     for line in process.stderr:
#         error_text.append(line)
#         error_area.text_area("Errors", "".join(error_text), height=300)

#     process.wait()


def run_command(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,   # <— merge stderr into stdout
        text=True,
        bufsize=1,
        encoding="utf-8",
        errors="replace"
    )

    output_area = st.empty()
    output_text = []

    # Read combined stdout+stderr line by line
    for line in process.stdout:
        output_text.append(line)
        output_area.text_area(
            "Processing Output (stdout + stderr)",
            "".join(output_text),
            height=300
        )

    process.stdout.close()
    process.wait()



def run_dump(pdfs, output_dir):
    if not pdfs or not output_dir:
        st.error("Please upload at least one PDF and specify an output directory.")
        return
    
    output_dir = os.path.abspath(output_dir)  # Ensure absolute path
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_paths = []
    for pdf in pdfs:
        pdf_path = os.path.join(output_dir, pdf.name)  # Save full path
        with open(pdf_path, "wb") as f:
            f.write(pdf.getbuffer())
        pdf_paths.append(pdf_path)
    
    command = [VENV_PYTHON, "automation.py", "dump", *pdf_paths, output_dir]
    run_command(command)

def run_search(query):
    command = [VENV_PYTHON, "automation.py", "search"]
    if query:
        command.append(query)
    
    run_command(command)

st.title("Research Paper Summarizer")

# Sidebar for Milvus Collections
st.sidebar.header("Database Collections")
client = get_milvus_client()

if client:
    collections = client.list_collections()
    selected_collection = st.sidebar.selectbox("Select a collection to delete", collections, index=None, placeholder="Select a collection...")

    if st.sidebar.button("Delete Collection"):
        st.session_state["delete_confirm"] = True  # Set flag to confirm

    if st.session_state.get("delete_confirm", False):
        st.sidebar.error(f"Do you really want delete {selected_collection}?")
        if st.sidebar.button("Yes"):
            client.drop_collection(collection_name=selected_collection)
            st.sidebar.success(f"Collection '{selected_collection}' deleted successfully!")
            del st.session_state["delete_confirm"]  # Reset flag
            st.rerun()  # Refresh the UI
        if st.sidebar.button("Cancel"):
            del st.session_state["delete_confirm"]  # Reset flag
            st.rerun()
else:
    st.sidebar.warning("Milvus connection unavailable. Ensure the server is running on localhost:19121")

st.header("Save Data Database")
uploaded_pdfs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
output_directory = st.text_input("Output Directory")
if st.button("Process PDFs"):
    run_dump(uploaded_pdfs, output_directory)

st.header("Search and Summarize")
query = st.text_input("Enter Search Query")
if st.button("Summarize"):
    run_search(query)
