from pdf2docx import Converter
from docx import Document
from weasyprint import HTML
import os
from datetime import datetime

OUTPUT_DIR = "converted_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_timestamped_filename(extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"output_{timestamp}.{extension}"

def convert_pdf_to_docx(pdf_file):
    filename = get_timestamped_filename("docx")
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())
    
    cv = Converter("temp.pdf")
    cv.convert(output_path, start=0, end=None)
    cv.close()
    
    os.remove("temp.pdf")
    return filename  # Return only the filename, not full path

def convert_docx_to_pdf(docx_file):
    filename = get_timestamped_filename("pdf")
    output_path = os.path.join(OUTPUT_DIR, filename)

    doc = Document(docx_file)
    doc.save("temp.docx")
    
    HTML(filename="temp.docx").write_pdf(output_path)
    os.remove("temp.docx")
    
    return filename

def convert_html_to_pdf(html_file):
    filename = get_timestamped_filename("pdf")
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    HTML(string=html_file.read().decode("utf-8")).write_pdf(output_path)
    
    return filename
