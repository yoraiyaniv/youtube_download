import yt_dlp

def download(url: str, download_path: str) -> None:
    ydl_opts = {
    'cookies': 'cookies.txt',
    'format': 'best',
    'outtmpl': download_path,
}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
