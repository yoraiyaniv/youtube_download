BIN_DIR = $(HOME)/.local/bin
FFMPEG_URL = https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz

set:
	pip install Flask
	pip install yt-dlp
	mkdir -p $(BIN_DIR)
	curl -L $(FFMPEG_URL) -o ffmpeg.tar.xz
	tar -xvf ffmpeg.tar.xz --strip-components=1 -C $(BIN_DIR)
	chmod +x $(BIN_DIR)/ffmpeg $(BIN_DIR)/ffprobe
	rm ffmpeg.tar.xz
