from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from log_parser import LogParser
from agent import IncidentAgent

app = FastAPI(title="AI Incident Investigation Agent")

# Directory setup
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Static & template mounting
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the upload page."""
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": None, "summary": None, "analysis": None}
    )


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    """Handle .log/.txt file upload, parse it, and show summary + AI analysis."""
    allowed_extensions = (".log", ".txt")
    summary = None
    analysis = None

    if not file.filename.lower().endswith(allowed_extensions):
        message = "Invalid file type. Please upload a .log or .txt file."
    else:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        parser = LogParser()
        lines = parser.load_log(file_path)
        summary = parser.summarize(lines)

        agent = IncidentAgent()
        analysis = agent.analyze(summary)

        message = "File uploaded successfully"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": message, "summary": summary, "analysis": analysis},
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)