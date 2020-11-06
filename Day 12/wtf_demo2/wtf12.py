from flask import Flask, request, render_template
from formValid import RegisterForm, LoginForm

app = Flask(__name__)


@app.route('/')
def index():
    return 'wtf home page'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # elif request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     password_verify = request.form.get('password_verify')
    #     if len(username) < 3 or len(username) > 10:
    #         return '用戶名長度不正確'
    #     if password != password_verify:
    #         return '兩次密碼不一致'
    #     if len(password) < 3 or len(password) > 10:
    #         return '密碼長度不正確'
    #     return
    else:
        form = RegisterForm(request.form)
        if form.validate():
            return '註冊成功'
        else:
            print(form.errors)
            return '註冊失敗'


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return '註冊成功'
        else:
            print(form.errors)
            return '註冊失敗'


if __name__ == '__main__':
    app.run(debug=True)
