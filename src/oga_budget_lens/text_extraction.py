import fitz
import json
import logging
from pathlib import Path
from oga_budget_lens.pdf_type import detect_page_type
logger = logging.getLogger(__name__)
def save_raw_artifact(data, pdf_path, page_number, method):
    base = Path(pdf_path).stem
    raw_dir = Path("data/intermediate/raw_extraction")
    raw_dir.mkdir(parents=True, exist_ok=True)
    file_path = raw_dir / f"{base}_page_{page_number}_{method}.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    return file_path
def extract_text_pipeline(pdf_path: str):
    output_pages = []
    with fitz.open(pdf_path) as doc:
        for page_number, page in enumerate(doc, start=1):
            extraction_method = detect_page_type(page)
            # DIGITAL TEXT EXTRACTION
            if extraction_method == "digital":
                words = page.get_text("words")
                save_raw_artifact(words, pdf_path, page_number, "digital")
                tokens = []
                for w in words:
                    x0, y0, x1, y1, word, *_ = w
                    tokens.append({
                        "text": word,
                        "x0": x0,
                        "y0": y0,
                        "x1": x1,
                        "y1": y1
                    })
                full_text = page.get_text("text")
                tool = "pymupdf"
            # OCR FALLBACK
            else:
                pix = page.get_pixmap()
                img_bytes = pix.tobytes("png")
                import pytesseract
                from PIL import Image
                import io
                image = Image.open(io.BytesIO(img_bytes))
                data = pytesseract.image_to_data(
                    image,
                    output_type=pytesseract.Output.DICT
                )
                save_raw_artifact(data, pdf_path, page_number, "ocr")
                tokens = []
                for i in range(len(data["text"])):
                    word = data["text"][i].strip()
                    if not word:
                        continue
                    tokens.append({
                        "text": word,
                        "x0": data["left"][i],
                        "y0": data["top"][i],
                        "x1": data["left"][i] + data["width"][i],
                        "y1": data["top"][i] + data["height"][i],
                        "confidence": data["conf"][i]
                    })
                full_text = " ".join([t["text"] for t in tokens])
                tool = "pytesseract"
            page_data = {
                "source_document": Path(pdf_path).name,
                "page_number": page_number,
                "extraction_method": extraction_method,
                "tool": tool,
                "full_text": full_text,
                "tokens": tokens
            }
            output_pages.append(page_data)
    return output_pages

def save_extraction_output(data, pdf_path):
    name = Path(pdf_path).stem
    output_dir = Path("data/intermediate/text_extraction")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{name}.json"
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
    logger.info("Saved extraction output to %s", output_file)
    return output_file