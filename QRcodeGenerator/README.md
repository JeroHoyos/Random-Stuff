# QR Generator

Simple web application to generate QR codes from a URL using FastAPI.

## Requirements:
- Python 3.10+
- pip

## Create and activate virtual environment (Windows):
    python -m venv .venv
    .venv\\Scripts\\activate

## Install dependencies:
    pip install -r requirements.txt

## Run the application:
    uvicorn main:app --reload

## Open in browser:
    http://127.0.0.1:8000

Usage:
1. Enter a URL
2. Enter a file name
3. Generate the QR code

The QR image is saved as a PNG file.