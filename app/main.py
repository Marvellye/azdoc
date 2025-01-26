import os
import logging
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from app.converters import convert_pdf_to_docx, convert_docx_to_pdf, convert_html_to_pdf

app = FastAPI()

# Directory for storing converted files
OUTPUT_DIR = "converted_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mount static files route
app.mount("/files", StaticFiles(directory=OUTPUT_DIR), name="files")

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "Welcome to Document Converter API"}

@app.post("/convert/pdf-to-docx")
async def pdf_to_docx(file: UploadFile = File(...)):
    filename = convert_pdf_to_docx(file.file)
    file_path = os.path.join(OUTPUT_DIR, filename)
    logging.info(f"Converted file saved at: {file_path}")
    return {"message": "Conversion successful", "file_url": f"/files/{filename}"}

@app.post("/convert/docx-to-pdf")
async def docx_to_pdf(file: UploadFile = File(...)):
    filename = convert_docx_to_pdf(file.file)
    file_path = os.path.join(OUTPUT_DIR, filename)
    logging.info(f"Converted file saved at: {file_path}")
    return {"message": "Conversion successful", "file_url": f"/files/{filename}"}

@app.post("/convert/html-to-pdf")
async def html_to_pdf(file: UploadFile = File(...)):
    filename = convert_html_to_pdf(file.file)
    file_path = os.path.join(OUTPUT_DIR, filename)
    logging.info(f"Converted file saved at: {file_path}")
    return {"message": "Conversion successful", "file_url": f"/files/{filename}"}
