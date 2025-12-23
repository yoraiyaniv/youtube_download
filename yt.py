import yt_dlp
import os

def download(url: str, download_path: str) -> None:
    base_path = os.path.dirname(os.path.abspath(__file__))
    local_ffmpeg = os.path.join(base_path, "bin", "ffmpeg")

    if os.path.exists(local_ffmpeg):
        print(f"DEBUG: Found FFmpeg at {local_ffmpeg}")
    else:
        # List files to help you debug if it's missing
        print(f"DEBUG: FFmpeg NOT FOUND at {local_ffmpeg}")
        if os.path.exists(os.path.join(base_path, "bin")):
            print(f"DEBUG: bin/ contains: {os.listdir(os.path.join(base_path, 'bin'))}")
    
    ydl_opts = {
        # 1. Correct the key to 'cookiefile'
        'cookiefile': 'cookies.txt', 
        
        # 2. Point to the FFmpeg you installed via Makefile
        'ffmpeg_location': local_ffmpeg,
        
        'format': 'best',
        'outtmpl': download_path,
        'noplaylist': True,
        
        # 3. Impersonate a browser to prevent immediate cookie invalidation
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
