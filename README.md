# "yt-dlp/Parabolic based" WebApp

Simple web app to download YouTube videos or audio using yt-dlp.

## Features

- FastAPI backend API
- Modern Svelte frontend
- No captcha (can be added)
- Dockerized with multi-stage build
- Ready for Render.com deployment

## Local development

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
