from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import mimetypes

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename, filepath):
    ext = filename.rsplit('.', 1)[-1].lower()
    mime = mimetypes.guess_type(filepath)[0]
    # Boleh file yang berekstensi gambar, tapi tidak cek isi file beneran
    return ext in {'jpg', 'jpeg', 'png', 'gif'}

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    if request.method == 'POST':
        if 'file' not in request.files:
            msg = 'No file part'
        else:
            file = request.files['file']
            if file.filename == '':
                msg = 'No selected file'
            else:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                if allowed_file(filename, filepath):
                    msg = f'Upload berhasil!<a href="/{filepath}">file</a>'
                else:
                    os.remove(filepath)
                    msg = 'Upload ditolak: Hanya gambar diperbolehkan.'
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500,debug=True)

