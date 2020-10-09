from flask import Flask, request
import uuid

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/list/<int:sid>')
def article(sid):
    return '這是第{}篇文章, uuid : {}' \
        .format(sid, uuid.uuid4())


@app.route('/<any(dict,tuple):url_path>/')
def item(url_path):
    return url_path


@app.route('/ie')
def baidu():
    return '{}{}'.format(request.args.get('name'), request.args.get('last'))


if __name__ == '__main__':
    app.run()

# 路由 : Url
