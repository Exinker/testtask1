import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from transformer import transformer

#
import librosa
import librosa.display as display
import matplotlib.pyplot as plt
import numpy as np

#
app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def upload():
    def allowed_file(filename):
        return ('.' in filename) and (filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS'])

    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            transformer(filepath=app.config['UPLOAD_FOLDER'], filename=filename)

            return redirect(url_for('uploads', filename=filename))

    return render_template('index.html', title='upload')

@app.route('/about')
def about():
    return render_template('about.html', title='about page')

@app.route('/uploads/<filename>')
def uploads(filename):

    return render_template(
        'uploads.html',
        src=os.path.join(os.sep, 'static', 'uploads', filename.split('.')[0] + '.png'),
    )
