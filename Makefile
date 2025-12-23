BIN_DIR = $(HOME)/.local/bin
FFMPEG_URL = https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
TEMP_DIR = ffmpeg_tmp

set:
	pip install Flask
	pip install yt-dlp
	pip install --user yt-dlp-get-oauth2

	mkdir -p $(BIN_DIR)

	mkdir -p $(TEMP_DIR)
	curl -L $(FFMPEG_URL) -o $(TEMP_DIR)/ffmpeg.tar.xz

	tar -xvf $(TEMP_DIR)/ffmpeg.tar.xz -C $(TEMP_DIR) --strip-components=1

	cp $(TEMP_DIR)/ffmpeg $(BIN_DIR)/
	cp $(TEMP_DIR)/ffprobe $(BIN_DIR)/
	chmod +x $(BIN_DIR)/ffmpeg $(BIN_DIR)/ffprobe

	rm -rf $(TEMP_DIR)
