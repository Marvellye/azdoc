from fastapi import FastAPI, File, UploadFile
from app.converters import convert_pdf_to_docx, convert_docx_to_pdf, convert_html_to_pdf
import shutil

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Document Converter API"}

@app.post("/convert/pdf-to-docx")
async def pdf_to_docx(file: UploadFile = File(...)):
    output_path = convert_pdf_to_docx(file.file)
    return {"message": "Conversion successful", "output": output_path}

@app.post("/convert/docx-to-pdf")
async def docx_to_pdf(file: UploadFile = File(...)):
    output_path = convert_docx_to_pdf(file.file)
    return {"message": "Conversion successful", "output": output_path}

@app.post("/convert/html-to-pdf")
async def html_to_pdf(file: UploadFile = File(...)):
    output_path = convert_html_to_pdf(file.file)
    return {"message": "Conversion successful", "output": output_path}
