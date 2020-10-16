from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/list/')
def list_article():
    return render_template('list_article.html')

if __name__ == '__main__':
    app.run(debug=True)
