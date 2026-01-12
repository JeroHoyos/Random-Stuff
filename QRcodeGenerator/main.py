from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import qrcode
import re

app = FastAPI()

# Carpetas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

QR_DIR = Path("static/qr")
QR_DIR.mkdir(parents=True, exist_ok=True)


def clean_filename(name: str) -> str:
    """Evita caracteres peligrosos en nombres de archivo"""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "qr": None}
    )


@app.post("/", response_class=HTMLResponse)
def generate_qr(
    request: Request,
    link: str = Form(...),
    filename: str = Form(...)
):
    filename = clean_filename(filename)
    file_path = QR_DIR / f"{filename}.png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "qr": f"/static/qr/{filename}.png",
            "filename": filename
        }
    )
