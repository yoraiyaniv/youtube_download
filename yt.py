import yt_dlp
import os

def download(url: str, download_path: str) -> None:
    home = os.path.expanduser("~")
    
    ydl_opts = {
        # 1. Correct the key to 'cookiefile'
        'cookiefile': 'cookies.txt', 
        
        # 2. Point to the FFmpeg you installed via Makefile
        'ffmpeg_location': f'{home}/.local/bin/ffmpeg',
        
        'format': 'best',
        'outtmpl': download_path,
        'noplaylist': True,
        
        # 3. Impersonate a browser to prevent immediate cookie invalidation
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
