from flask import Flask, session, request, current_app, g
import os
from datetime import timedelta
from utils import log_a, log_b

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

print(app)
# 在外應用上下文
with app.app_context():
    app2 = current_app
    print(app2)


@app.route('/')
def index():
    # session 保存用戶信息
    username = session.get('username')
    g.username = username
    # 在內應用上下文
    # print(current_app.name)
    log_a()
    log_b()
    hello()
    return 'Session Index {}'.format(username)

def hello():
    print('hello {}'.format(g.username))


@app.route('/login/')
def login():
    # session is dist
    session['username'] = 'Jason'
    # session 過期時間設置，預設為一個月，可加入config設定過期時間
    # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
    session.permanent = True
    return 'Login page'


@app.route('/logout/')
def logout():
    # 刪除Key
    session.pop('username')
    # 清空Session
    session.clear()
    return 'Logout page'


if __name__ == '__main__':
    app.run(debug=True)
