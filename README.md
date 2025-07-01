# yt-dlp/Parabolic based Web App

A simple web application to download video or audio from YouTube using `yt-dlp`, with optional reCAPTCHA protection.

## 🛠 Tech Stack
- FastAPI (backend)
- Plain HTML/CSS (dark UI inspired by Parabolic)
- yt-dlp for YouTube downloads
- Google reCAPTCHA support (optional)

## 🚀 Quick Deploy
1. Create a `.env` file with your `RECAPTCHA_SECRET`
2. Push the project to GitHub
3. Deploy on [Render](https://render.com) using `render.yaml`

## 🧪 API Usage
POST `/api/download`
```json
{
  "url": "https://youtube.com/watch?v=...",
  "format": "best" | "bestaudio",
  "token": "captcha-response"
}
```

## 🔒 Security
- CAPTCHA support helps block bots
- Downloaded files are temporary and automatically removed

---
MIT License
