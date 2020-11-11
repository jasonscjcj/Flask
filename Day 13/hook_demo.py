from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    a = 1 / 0
    print('hook page')
    # return 'hook page'
    return render_template('index.html')


@app.route('/login/')
def login():
    print('login page')
    # return 'hook page'
    return render_template('login.html')


@app.before_first_request
def before_first_request():
    print('這是請求之前第一個執行的函數')
    # return '這是請求之前第一個執行的函數'


@app.before_request
def before_request():
    print('這是請求之前執行的函數')
    # return '這是請求之前執行的函數'


@app.after_request
def after_request(res):
    print('這是請求之後執行的函數 {}'.format(res))
    return res


# 有沒有報錯都會返回
@app.teardown_request
def teardown_request(res):
    print('有沒有報錯都會返回 {}'.format(res))
    return res


@app.context_processor
def context_processor():
    return {'username': 'Jason'}


@app.errorhandler(404)
def errorhandler(errorcode):
    # return render_template('404.html')
    return '你找的網頁不存在:{}'.format(errorcode), 404


@app.errorhandler(500)
def server_error(errorcode):
    return '服務器錯誤 : {}'.format(errorcode), 500


if __name__ == '__main__':
    app.run(debug=False)
