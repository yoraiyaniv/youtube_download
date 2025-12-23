PROJECT_BIN = $(shell pwd)/bin
FFMPEG_URL = https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz

set:
	pip install Flask
	pip install yt-dlp
	mkdir -p $(PROJECT_BIN)
	curl -L $(FFMPEG_URL) -o ffmpeg.tar.xz
	tar -xvf ffmpeg.tar.xz --strip-components=1 -C $(PROJECT_BIN)
	chmod +x $(PROJECT_BIN)/ffmpeg $(PROJECT_BIN)/ffprobe
	rm ffmpeg.tar.xz
	@echo "FFmpeg installed to: $(PROJECT_BIN)/ffmpeg"
