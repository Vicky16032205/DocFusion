# import os
# import re
# import subprocess

# def md_to_latex(md_file, tex_file, pdf_file):
#     output_dir = os.path.dirname(tex_file)  # Get the output directory from tex_file
#     os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

#     with open(md_file, 'r', encoding='utf-8') as f:
#         md_content = f.readlines()

#     tex_content = [
#         "\\documentclass{article}\n",
#         "\\usepackage{arxiv}\n",
#         "\\usepackage{graphicx}\n",
#         "\\usepackage{amsmath,amssymb}\n",
#         "\\usepackage{hyperref}\n",
#         "\\usepackage{multicol}\n",
#         "\\usepackage[numbers]{natbib}\n",
#         "\\begin{document}\n"
#     ]

#     title = None
#     body_content = []
#     references_section = False
#     references = []
#     citation_map = {}  # Keeps track of citation numbers
#     figure_counter = 1  # Auto-number figures

#     for i, line in enumerate(md_content):
#         line = line.strip()
#         line = line.replace("&", "\\&")  # Escape '&' to prevent LaTeX errors

#         # Convert bold (**word**) and italic (*word*) text to LaTeX format
#         line = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", line)  # Bold
#         line = re.sub(r"\*(.*?)\*", r"\\textit{\1}", line)  # Italic

#         # Detect Title
#         if line.startswith("# "):
#             title = line[2:]
        
#         # Detect Section Headers
#         elif line.startswith("## "):
#             if line.strip() == "## References":
#                 references_section = True
#                 body_content.append("\\begin{thebibliography}{99}\n")
#             else:
#                 body_content.append(f"\\section*{{{line[3:]}}}\n")
        
#         elif line.startswith("### "):
#             body_content.append(f"\\subsection*{{{line[4:]}}}\n")

#         # Handle References
#         elif references_section:
#             match = re.match(r"\[(\d+)\] (.+)", line)
#             if match:
#                 ref_id, ref_text = match.groups()
#                 citation_map[ref_id] = ref_id  # Keep reference numbering unchanged
#                 references.append(f"\\bibitem{{{ref_id}}} {ref_text}\n")
        
#         # Handle Images and Captions
#         elif re.match(r"!\[.*\]\((.*?)\)", line):  
#             # Extract image path
#             img_match = re.match(r"!\[.*\]\((.*?)\)", line)
#             img_path = img_match.group(1)

#             # Convert Windows path to LaTeX-compatible relative path
#             img_path = img_path.replace("\\", "/")  

#             # Check if next line is a caption
#             caption = ""
#             if i + 1 < len(md_content) and "**Figure Caption:**" in md_content[i + 1]:
#                 caption = re.sub(r"\*\*Figure Caption:\*\*\s*", "", md_content[i + 1].strip())

#             # Add image to LaTeX
#             body_content.append("\\begin{figure}[h]\n\\centering\n")
#             body_content.append(f"\\includegraphics[width=0.9\\linewidth]{{{img_path}}}\n")
#             if caption:
#                 body_content.append(f"\\caption{{Figure {figure_counter}: {caption}}}\n")
#                 figure_counter += 1  # Increment figure number
#             body_content.append("\\end{figure}\n\n")

#         else:
#             # Convert inline citations [1] → \cite{1} (Only if not in References)
#             line = re.sub(r"\[(\d+)\]", lambda m: f"\\cite{{{m.group(1)}}}", line)
#             body_content.append(line + '\n')

#     # if references:
#     #     body_content.append("\n".join(references))
#     #     body_content.append("\\end{thebibliography}\n")

#     if references:
#         body_content.append("\\begin{thebibliography}{99}\n")
#         body_content.append("\n".join(references))
#         body_content.append("\\end{thebibliography}\n")
#     else:
#         # If no references, just skip the bibliography entirely
#         pass

#     # Add title and author at the top
#     if title:
#         tex_content.append(f"\\title{{{title}}}\n")
#     tex_content.append("\\author{Artificial Intelligence}\n")
#     tex_content.append("\\date{\\today}\n")
#     tex_content.append("\\maketitle\n")
#     tex_content.append("\\noindent\n")
#     tex_content.append("\\twocolumn\n")

#     # Append main content
#     tex_content.extend(body_content)
#     tex_content.append("\n\\end{document}\n")

#     # Save LaTeX file inside output directory
#     with open(tex_file, 'w', encoding='utf-8') as f:
#         f.writelines(tex_content)

#     print(f"LaTeX file saved as {tex_file}")

#     # Ensure all generated files go to the output directory
#     pdf_output_path = os.path.join(output_dir, os.path.basename(pdf_file))

#     # Compile LaTeX to PDF (Twice for correct citations)
#     subprocess.run(["pdflatex", "-output-directory", output_dir, tex_file])
#     subprocess.run(["pdflatex", "-output-directory", output_dir, tex_file])

#     print(f"PDF generated: {pdf_output_path}")























# ToLatex.py
import os
import re
import subprocess

def md_to_latex(md_file, tex_file, pdf_file):
    output_dir = os.path.dirname(tex_file)
    os.makedirs(output_dir, exist_ok=True)

    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.readlines()

    tex_content = [
        "\\documentclass{article}\n",
        "\\usepackage{arxiv}\n",
        "\\usepackage{graphicx}\n",
        "\\usepackage{amsmath,amssymb}\n",
        "\\usepackage{hyperref}\n",
        "\\usepackage{multicol}\n",
        "\\usepackage[numbers]{natbib}\n",
        "\\begin{document}\n"
    ]

    title = None
    body_content = []
    references_section = False
    references = []
    figure_counter = 1

    for i, line in enumerate(md_content):
        original_line = line
        line = line.strip()
        if not line:
            if not references_section:
                body_content.append("\n")
            continue

        # Escape special LaTeX characters
        line = line.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#")

        # Bold and Italic
        line = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", line)
        line = re.sub(r"\*(.*?)\*", r"\\textit{\1}", line)

        # Title
        if line.startswith("# ") and not title:
            title = line[2:].strip()

        # Main sections (## )
        elif line.startswith("## "):
            header_text = line[3:].strip()
            if header_text == "References":
                references_section = True
                # DO NOT add \begin{thebibliography} here!
                body_content.append(f"\\section*{{{header_text}}}\n")
            else:
                references_section = False
                body_content.append(f"\\section*{{{header_text}}}\n")

        # Subsections (### )
        elif line.startswith("### "):
            body_content.append(f"\\subsection*{{{line[4:].strip()}}}\n")

        # Handle references [1] Author...
        elif references_section:
            match = re.match(r"\[(\d+)\]\s*(.+)", line)
            if match:
                ref_id, ref_text = match.groups()
                ref_text = ref_text.strip()
                if ref_text:
                    references.append(f"\\bibitem{{{ref_id}}} {ref_text}\n")

        # Handle images
        elif re.match(r"!\[.*\]\((.*?)\)", line):
            img_match = re.match(r"!\[.*\]\((.*?)\)", line)
            img_path = img_match.group(1).replace("\\", "/")

            caption = ""
            if i + 1 < len(md_content) and md_content[i + 1].strip().startswith("**Figure Caption:**"):
                caption = md_content[i + 1].strip()
                caption = re.sub(r"\*\*Figure Caption:\*\*\s*", "", caption)

            body_content.append("\\begin{figure}[h]\n\\centering\n")
            body_content.append(f"\\includegraphics[width=0.9\\linewidth]{{{img_path}}}\n")
            if caption:
                body_content.append(f"\\caption{{Figure {figure_counter}: {caption}}}\n")
                figure_counter += 1
            else:
                body_content.append(f"\\caption{{Figure {figure_counter}}}\n")
                figure_counter += 1
            body_content.append("\\end{figure}\n\n")

        # Normal text + citation conversion [1] → \cite{1}
        else:
            if not references_section:
                line = re.sub(r"\[(\d+)\]", r"\\cite{\1}", line)
            body_content.append(line + "\n")

    # === ONLY ADD BIBLIOGRAPHY IF WE HAVE ACTUAL REFERENCES ===
    if references:
        body_content.append("\\begin{thebibliography}{99}\n")
        body_content.extend(references)
        body_content.append("\\end{thebibliography}\n")

    # Title and metadata
    if title:
        tex_content.append(f"\\title{{{title}}}\n")
    tex_content.append("\\author{Artificial Intelligence}\n")
    tex_content.append("\\date{\\today}\n")
    tex_content.append("\\maketitle\n")
    tex_content.append("\\noindent\n")
    tex_content.append("\\twocolumn\n")

    # Add all content
    tex_content.extend(body_content)
    tex_content.append("\\end{document}\n")

    # Write .tex file
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.writelines(tex_content)

    print(f"LaTeX file saved: {tex_file}")

    # Compile to PDF (twice for citations)
    try:
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", output_dir, tex_file], 
                      check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", output_dir, tex_file], 
                      check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"PDF generated successfully: {pdf_file}")
    except subprocess.CalledProcessError:
        print("PDF compilation had warnings/errors, but file may still be generated.")

    print("Review paper ready! Open latex-output/output.pdf")