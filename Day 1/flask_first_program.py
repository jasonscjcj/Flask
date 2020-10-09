from flask import Flask
import config

# __name__ = '__main__'

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    app.config.from_pyfile('config.py', silent=True)
    app.run()
