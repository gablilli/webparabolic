from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend.yt_downloader import download_video
import os
import uuid
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

RECAPTCHA_SECRET = os.getenv("6Lf03HQrAAAAAJ_jSunX_V6VhNgormVRzVGjLKc8")

@app.post("/api/download")
async def download(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    url = data.get("url")
    format = data.get("format", "best")
    token = data.get("token")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    if RECAPTCHA_SECRET and token:
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data={
            "secret": RECAPTCHA_SECRET,
            "response": token
        })
        if not r.json().get("success"):
            raise HTTPException(status_code=403, detail="Captcha failed")

    uid = str(uuid.uuid4())
    output_path = f"public/downloads/{uid}.%(ext)s"

    filename = download_video(url, output_path, format)
    if not filename:
        raise HTTPException(status_code=500, detail="Download failed")

    def cleanup():
        try:
            os.remove(filename)
        except:
            pass

    background_tasks.add_task(cleanup)
    return FileResponse(filename, filename=os.path.basename(filename), media_type='application/octet-stream')
