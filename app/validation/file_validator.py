import os
import mimetypes

ALLOWED_EXTENSIONS = {".pdf"}
ALLOWED_MIME_TYPES = {"application/pdf"}

class FileValidationError(Exception):
    """Custom exception for file validation errors."""
    pass


def validate_file(filename: str, file_content: bytes = None):
    """
    Validate uploaded file.

    Args:
        filename (str): Name of uploaded file
        file_content (bytes): Optional file content for deeper validation

    Returns:
        dict: validation result
    """

    if not filename:
        raise FileValidationError("Uploaded file must have a valid filename.")

    # Extension validation
    ext = os.path.splitext(filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise FileValidationError(
            f"Unsupported file type '{ext}'. Only PDF files are allowed."
        )

    # MIME type validation
    mime_type, _ = mimetypes.guess_type(filename)

    if mime_type not in ALLOWED_MIME_TYPES:
        raise FileValidationError(
            f"Invalid MIME type '{mime_type}'. Expected a PDF document."
        )

    return {
        "filename": filename,
        "extension": ext,
        "mime_type": mime_type,
        "is_valid": True
    }