from flask import Flask, request, send_file
from yt import download
import uuid
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    output_path = "downloads/%s.mp4" %(uuid.uuid4())
    download(request.args.get("url"), output_path)
    resp = send_file(output_path)
    os.remove(output_path)
    return resp

if __name__ == "__main__":
    app.run(debug=False, port=80, host='0.0.0.0')