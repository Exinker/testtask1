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
        print('filename:', file.filename)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
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
        filepath='{0}static{0}uploads{0}'.format(os.path.sep),
        filename=filename.split('.')[0] + '.png',
    )
