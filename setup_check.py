"""
Environment Setup Verification Script
This script checks if all required dependencies are properly installed.
"""

import sys

def check_python_version():
    """Check if Python version is 3.10 or higher"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version {version.major}.{version.minor} is too old. Requires 3.10+")
        return False

def check_imports():
    """Check if all required packages can be imported"""
    packages = [
        "fastapi",
        "uvicorn",
        "pdfplumber",
        "camelot",
        "pytesseract",
        "pandas",
        "langdetect",
        "pytest",
        "cv2",
        "fitz",
    ]
    
    all_good = True
    for package in packages:
        try:
            __import__(package)
            print(f"✓ {package} imported successfully")
        except ImportError:
            print(f"✗ {package} failed to import")
            all_good = False
    
    return all_good

def main():
    print("=" * 50)
    print("OGA Budget Lens - Environment Check")
    print("=" * 50)
    print()
    
    python_ok = check_python_version()
    print()
    imports_ok = check_imports()
    print()
    
    if python_ok and imports_ok:
        print("=" * 50)
        print("✓ All checks passed! Environment ready.")
        print("=" * 50)
        return 0
    else:
        print("=" * 50)
        print("✗ Some checks failed. Please review above.")
        print("=" * 50)
        return 1

if __name__ == "__main__":
    sys.exit(main())