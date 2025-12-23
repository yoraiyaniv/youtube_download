import yt_dlp
import os

def download(url: str, download_path: str) -> None:
    home = os.path.expanduser("~")
    
    ydl_opts = {
        # USE THE BUILT-IN OAUTH2 (No plugin required)
        'username': 'oauth2',
        'password': '', 
        
        # Use the 'tv' client - this is the most reliable for OAuth2
        'extractor_args': {
            'youtube': {
                'player_client': ['tv'],
            }
        },
        
        'ffmpeg_location': f'{home}/.local/bin/ffmpeg',
        'format': 'best',
        'outtmpl': download_path,
        'verbose': True, # CRITICAL: This ensures the code shows in your logs
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
