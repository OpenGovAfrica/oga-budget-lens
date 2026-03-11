from fastapi import FastAPI, HTTPException
from oga_budget_lens.pdf_type import detect_pdf_type
from app.validation.file_validator import validate_file, FileValidationError
import os

app = FastAPI(title="OGA Budget Lens API")


@app.get("/")
def read_root():
    return {"message": "Welcome to OGA Budget Lens API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/detect")
def detect(filename: str):
    
    try:
        validate_file(filename)
    except FileValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

    path = os.path.join("/data/samples", filename)

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")

    result = detect_pdf_type(path)
    return result