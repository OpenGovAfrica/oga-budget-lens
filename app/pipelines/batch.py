import os
import sys
import json
import traceback

from oga_budget_lens.pdf_type import detect_pdf_type
from oga_budget_lens.text_extraction import extract_text_pipeline
from app.services.table_detection import TableDetector


def run_pipeline(data_dir: str = "data/samples"):
    print(f"Starting batch pipeline on directory: {data_dir}")

    if not os.path.exists(data_dir):
        print(f"Error: Directory {data_dir} not found.")
        sys.exit(1)

    files = [f for f in os.listdir(data_dir) if f.lower().endswith('.pdf')]

    if not files:
        print(f"No PDF files found in {data_dir}")
        return

    os.makedirs("data/output", exist_ok=True)
    detector = TableDetector()

    for filename in files:
        path = os.path.join(data_dir, filename)

        print("\n" + "=" * 50)
        print(f"Processing: {filename}")

        try:
            pdf_info = detect_pdf_type(path)
            pages = extract_text_pipeline(path)

            if not pages:
                print(f"No pages extracted from {filename}")
                continue

            all_tables = [detector.detect(page) for page in pages]

            total_tables = sum(len(p.get("tables", [])) for p in all_tables)

            print(f"Type: {pdf_info['pdf_type']}")
            print(f"Pages: {len(pages)}")
            print(f"Tables detected: {total_tables}")

            if all_tables and all_tables[0].get("tables"):
                sample_rows = all_tables[0]["tables"][0]["rows"][:1]
                print("Sample row:", sample_rows)

            output = {
                "file": filename,
                "pdf_type": pdf_info["pdf_type"],
                "total_pages": len(pages),
                "tables": all_tables
            }

            name = os.path.splitext(filename)[0]
            output_file = f"data/output/{name}.json"

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2)

            print(f"Saved output to {output_file}")

        except Exception as e:
            print(f"[ERROR] {filename}: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    data_directory = sys.argv[1] if len(sys.argv) > 1 else "data/samples"
    run_pipeline(data_directory)
