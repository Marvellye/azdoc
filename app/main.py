from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.converters import convert_pdf_to_docx, convert_docx_to_pdf, convert_html_to_pdf
import shutil
import os

app = FastAPI()

# Directory to store converted files
OUTPUT_DIR = "converted_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mount static files route for serving converted files
app.mount("/files", StaticFiles(directory=OUTPUT_DIR), name="files")

@app.get("/")
def read_root():
    return {"message": "Welcome to Document Converter API"}

@app.post("/convert/pdf-to-docx")
async def pdf_to_docx(file: UploadFile = File(...)):
    output_path = os.path.join(OUTPUT_DIR, convert_pdf_to_docx(file.file))
    return {"message": "Conversion successful", "file_url": f"/files/{os.path.basename(output_path)}"}

@app.post("/convert/docx-to-pdf")
async def docx_to_pdf(file: UploadFile = File(...)):
    output_path = os.path.join(OUTPUT_DIR, convert_docx_to_pdf(file.file))
    return {"message": "Conversion successful", "file_url": f"/files/{os.path.basename(output_path)}"}

@app.post("/convert/html-to-pdf")
async def html_to_pdf(file: UploadFile = File(...)):
    output_path = os.path.join(OUTPUT_DIR, convert_html_to_pdf(file.file))
    return {"message": "Conversion successful", "file_url": f"/files/{os.path.basename(output_path)}"}
