import fitz  # PyMuPDF
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def detect_pdf_type(path: str, max_pages: int = 5) -> dict:
    if not Path(path).is_file():
        raise FileNotFoundError(f"PDF not found: {path}")

    pages_checked = 0
    pages_with_text = 0

    try:
        with fitz.open(path) as doc:
            for page in doc:
                if pages_checked >= max_pages:
                    break

                text = page.get_text().strip()
                pages_checked += 1

                has_text = (
                    len(text.split()) > 10
                    and any(c.isalpha() for c in text)
                )

                if has_text:
                    pages_with_text += 1

    except fitz.FileDataError:
        raise ValueError(f"Invalid or corrupted PDF file: {path}")
    except RuntimeError:
        raise ValueError(f"Unable to process PDF (possibly encrypted): {path}")

    if pages_checked == 0:
        logger.warning("No readable pages found in PDF: %s", path)
        return {"pdf_type": "scanned", "text_page_ratio": 0.0}

    ratio = pages_with_text / pages_checked
    pdf_type = "digital" if ratio >= 0.5 else "scanned"

    logger.info(
        "PDF classified as %s with text_page_ratio %.2f (%d/%d pages contained text)",
        pdf_type,
        ratio,
        pages_with_text,
        pages_checked,
    )

    return {
        "pdf_type": pdf_type,
        "text_page_ratio": round(ratio, 2),
    }