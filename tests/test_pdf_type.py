import pytest
pytest.importorskip("fitz")

from oga_budget_lens.pdf_type import detect_pdf_type



def test_kenya_budget_is_digital():
    result = detect_pdf_type("data/samples/kenya_budget_2023_24.pdf")
    assert result["pdf_type"] == "digital"
    assert result["text_page_ratio"] >= 0.5


def test_south_africa_budget_is_digital():
    result = detect_pdf_type("data/samples/south_africa_budget_2025_overview.pdf")
    assert result["pdf_type"] == "digital"


def test_scanned_budget_kenya_pdf_is_detected():
    result = detect_pdf_type("data/samples/scanned_budget_kenya.pdf")
    assert result["pdf_type"] == "scanned"
