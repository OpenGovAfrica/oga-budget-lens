import os
import sys
from oga_budget_lens.pdf_type import detect_pdf_type

def run_pipeline(data_dir: str = "/data/samples"):
    print(f"Starting batch pipeline on directory: {data_dir}")
    if not os.path.exists(data_dir):
        print(f"Error: Directory {data_dir} not found.")
        sys.exit(1)
    
    files = [f for f in os.listdir(data_dir) if f.lower().endswith('.pdf')]
    if not files:
        print(f"No PDF files found in {data_dir}")
        return

    for filename in files:
        path = os.path.join(data_dir, filename)
        print(f"Processing: {filename}...")
        try:
            result = detect_pdf_type(path)
            print(f"File: {filename} | Type: {result['pdf_type']} | Ratio: {result['text_page_ratio']}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    data_directory = sys.argv[1] if len(sys.argv) > 1 else "/data/samples"
    run_pipeline(data_directory)
