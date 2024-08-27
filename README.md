Simple script to turn photo (not OCR) scanned PDFs into text.

1. Create a virtual environment:

```bash
python -m venv pdf_ocr_env
```

2. Activate the virtual environment:

On Windows:
```
pdf_ocr_env\Scripts\activate
```

On macOS and Linux:
```bash
source pdf_ocr_env/bin/activate
```

3. Install the requirements:

```bash
pip install -r requirements.txt
```

4. Install Tesseract OCR:

This script uses Tesseract OCR, which needs to be installed separately:

- On Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
- On macOS: `brew install tesseract`
- On Ubuntu: `sudo apt-get install tesseract-ocr`

5. You may also need to install Poppler:

- On Windows: Download from http://blog.alivate.com.au/poppler-windows/ and add to PATH
- On macOS: `brew install poppler`
- On Ubuntu: `sudo apt-get install poppler-utils`

After completing these steps, you should be ready to run the script in your virtual environment.