import os
import time
from flask import Flask, send_file, make_response
from pathlib import Path

app = Flask(__name__)

IMAGES_DIR = Path("./images")
ROTATION_INTERVAL = int(os.getenv("ROTATION_INTERVAL", "86400"))  # seconds (default: 1 day)

# Preload image list
images = sorted([p for p in IMAGES_DIR.iterdir() if p.is_file()])
if not images:
    raise RuntimeError(f"No images found in {IMAGES_DIR}")

start_time = time.time()

@app.route("/")
def serve_image():
    if not images:
        return "No images available", 404

    elapsed = time.time() - start_time
    index = int(elapsed // ROTATION_INTERVAL) % len(images)
    current_image = images[index]

    # Serve image with no-cache headers
    response = make_response(send_file(current_image, mimetype=f"image/{current_image.suffix[1:]}"))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767)