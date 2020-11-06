from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    res = Response('淘宝網')
    res.set_cookie(key='username', value='jason', max_age=60*60*24*7)
    return res


if __name__ == '__main__':
    app.run(debug=True)
