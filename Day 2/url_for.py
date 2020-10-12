from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    print(url_for('article', aid=1))    # /article/1
    print(url_for('article', aid=1, page=1))    # /article/1?page=1
    print(url_for('article', aid=1, page=1, name=1))    # /article/1?page=1&name=1
    print(url_for('article', aid=1, page=1, name=1, type=1))    # /article/1?page=1&name=1&type=1
    return 'Hello World!!!'


@app.route('/article/<string:aid>')
def article(aid):
    print(url_for('home', next='/'))    # /?next=%2F
    return 'article list 1 - {}'.format(aid)


if __name__ == '__main__':
    app.run(debug=True)
