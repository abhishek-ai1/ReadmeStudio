import os
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import markdown as md
from starlette.background import BackgroundTask
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

app = FastAPI()

# Get absolute paths for static and templates directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# CORS (optional, for local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("editor.html", {"request": request, "markdown_text": "", "html_preview": "", "year": datetime.now().year})

@app.post("/preview", response_class=HTMLResponse)
def preview(request: Request, markdown_text: str = Form(...)):
    html_preview = md.markdown(markdown_text, extensions=["extra", "toc", "tables"])
    return templates.TemplateResponse("editor.html", {"request": request, "markdown_text": markdown_text, "html_preview": html_preview, "year": datetime.now().year})

@app.post("/upload", response_class=HTMLResponse)
def upload(request: Request, file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8")
    html_preview = md.markdown(content, extensions=["extra", "toc", "tables"])
    return templates.TemplateResponse("editor.html", {"request": request, "markdown_text": content, "html_preview": html_preview, "year": datetime.now().year})

@app.post("/export/md")
def export_md(markdown_text: str = Form(...)):
    return StreamingResponse(
        iter([markdown_text]),
        media_type="text/markdown",
        headers={"Content-Disposition": "attachment; filename=README.md"}
    )

@app.post("/export/html")
def export_html(markdown_text: str = Form(...)):
    html_content = md.markdown(markdown_text, extensions=["extra", "toc", "tables"])
    return StreamingResponse(
        iter([html_content]),
        media_type="text/html",
        headers={"Content-Disposition": "attachment; filename=README.html"}
    )

@app.post("/export/pdf")
def export_pdf(markdown_text: str = Form(...)):
    html_content = md.markdown(markdown_text, extensions=["extra", "toc", "tables"])
    pdf_file = os.path.join(UPLOAD_DIR, "README.pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    # Split the HTML content into lines (as plain text)
    lines = html_content.split("\n")
    y = height - 40  # Start from top
    for line in lines:
        # Remove HTML tags for plain text output
        import re
        clean_line = re.sub('<[^<]+?>', '', line)
        c.drawString(40, y, clean_line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()
    def cleanup():
        try:
            os.remove(pdf_file)
        except Exception:
            pass
    return FileResponse(pdf_file, media_type="application/pdf", filename="README.pdf", background=BackgroundTask(cleanup)) 