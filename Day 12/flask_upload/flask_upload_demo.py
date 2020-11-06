import os

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from forms import UploadForm
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)


@app.route('/')
def index():
    return 'UPLOAD首頁'


@app.route('/upload/', methods=["GET", "POST"])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # desc = request.form.get('desc')
        # image_file = request.files.get('image_file')
        # filename = secure_filename(image_file.filename)
        # image_file.save(os.path.join('images', filename))
        # return '文件保存成功'
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        print(form)
        if form.validate():
            desc = request.form.get('desc')
            image_file = request.files.get('image_file')
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join('images', filename))
            return '文件保存成功'
        else:
            print(form.errors)
            return '文件格式不正確'


if __name__ == '__main__':
    app.run(debug=True)
