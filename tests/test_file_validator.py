import pytest
from app.validation.file_validator import validate_file, FileValidationError


def test_valid_pdf_file():
    result = validate_file("budget.pdf")
    assert result["is_valid"] == True
    assert result["extension"] == ".pdf"


def test_invalid_extension():
    with pytest.raises(FileValidationError):
        validate_file("sample.txt")


def test_empty_filename():
    with pytest.raises(FileValidationError):
        validate_file("")


def test_wrong_mime_type():
    with pytest.raises(FileValidationError):
        validate_file("document.docx")