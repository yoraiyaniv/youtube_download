import yt_dlp
import os

def download(url: str, download_path: str) -> None:
    # Get home directory for ffmpeg path if needed
    home = os.path.expanduser("~")
    
    ydl_opts = {
        # 1. THE SMART FIX: Use OAuth2 instead of a cookie file
        'username': 'oauth2',
        'password': '', 
        
        # 2. Add client impersonation to bypass bot checks
        'extractor_args': {
            'youtube': {
                'player_client': ['ios', 'web']
            }
        },
        
        # 3. Reference your local ffmpeg from your Makefile install
        'ffmpeg_location': f'{home}/.local/bin/ffmpeg',
        
        'format': 'best',
        'outtmpl': download_path,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error during download: {e}")
