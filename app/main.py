from fastapi import FastAPI
from oga_budget_lens.pdf_type import detect_pdf_type
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
    # Search in /data/samples by default
    path = os.path.join("/data/samples", filename)
    if not os.path.exists(path):
        return {"error": "File not found"}
    
    result = detect_pdf_type(path)
    return result
