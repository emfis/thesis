import os
from flask import (
    Blueprint, request, flash, redirect, jsonify
)
from PIL import Image
from werkzeug.utils import secure_filename
import subprocess

bp = Blueprint('convert', __name__, url_prefix='/convert')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/simple', methods=['POST'])
def simple():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return {
                "error": "NO FILE",
                "request": request.files
            }
        file = request.files['image']
        img = Image.open(file.stream)
        # Run the model on the image here
        return jsonify({'msg': 'success', 'size': [img.width, img.height]})


