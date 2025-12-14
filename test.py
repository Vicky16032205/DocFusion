# test.py
import fitz
print("PyMuPDF version:", fitz.version)
doc = fitz.open(r"C:\Users\Rohan\Desktop\Research-Paper-Summarizer-main\Research-Paper-Summarizer-main\data\cnn5.pdf")
print(f"SUCCESS! PDF has {len(doc)} pages")
doc.close()