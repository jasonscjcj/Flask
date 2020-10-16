from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'username': 'Jason'
    }
    return render_template('index.html', **context)


@app.route('/list/')
def list_article():
    return render_template('list.html')


@app.route('/article/')
def article():
    return render_template('article.html')


if __name__ == '__main__':
    app.run(debug=True)
