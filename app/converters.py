from pdf2docx import Converter
from docx import Document
from weasyprint import HTML
import os

def convert_pdf_to_docx(pdf_file):
    output_path = "output.docx"
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())
    cv = Converter("temp.pdf")
    cv.convert(output_path, start=0, end=None)
    cv.close()
    os.remove("temp.pdf")
    return output_path

def convert_docx_to_pdf(docx_file):
    doc = Document(docx_file)
    output_path = "output.pdf"
    doc.save("temp.docx")
    HTML(filename="temp.docx").write_pdf(output_path)
    os.remove("temp.docx")
    return output_path

def convert_html_to_pdf(html_file):
    output_path = "output.pdf"
    HTML(string=html_file.read().decode("utf-8")).write_pdf(output_path)
    return output_path