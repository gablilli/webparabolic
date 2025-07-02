from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from backend.yt_downloader import download_video
import os
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

@app.post("/api/download")
async def download(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    url = data.get("url")
    format = data.get("format", "best")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

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

@app.get("/")
async def root():
    return JSONResponse({"status": "ok"})
