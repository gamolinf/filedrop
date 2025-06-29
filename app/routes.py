import os
from flask import Blueprint, request, jsonify, send_from_directory, current_app, render_template_string

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template_string('''
    <h1>Upload Image</h1>
    <form method="POST" action="/upload" enctype="multipart/form-data">
      <input type="file" name="image" accept="image/*" required>
      <button type="submit">Upload</button>
    </form>
    ''')

@bp.route('/images/<path:filename>')
def send_img(file_name):
    directory = current_app.config['UPLOAD_FOLDER']
    return send_from_directory(directory, file_name, as_attachment=True)

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    filename = file.filename
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    return f'/uploads/{filename}'