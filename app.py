import os
import cv2
import numpy as np
import face_recognition
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.secret_key = "your_secret_key"

# Ensure uploads folder exists
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

def process_image(image_path):
    """Detect and encode faces from an image."""
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        flash("No image uploaded", "danger")
        return redirect(url_for("home"))

    file = request.files["image"]
    if file.filename == "":
        flash("No selected file", "danger")
        return redirect(url_for("home"))

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    encodings = process_image(file_path)
    if encodings:
        flash("Face detected!", "success")
    else:
        flash("No face found!", "danger")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)