import yt_dlp
import glob

def download_video(url: str, output_path: str, format: str = "best") -> str:
    try:
        ydl_opts = {
            'format': format,
            'outtmpl': output_path,
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        base = output_path.split("%")[0]
        files = glob.glob(base + "*")
        return files[0] if files else None
    except Exception as e:
        print("Error:", e)
        return None
