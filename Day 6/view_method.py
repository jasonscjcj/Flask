from flask import Flask, views, render_template, request

app = Flask(__name__)


# 登錄之后才能訪問的裝飾器
def login_required(func):
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username:
            return func(*args, **kwargs)
        else:
            return '請先登錄'

    return wrapper


@app.route('/profile/')
@login_required
def settings():
    return '個人中心設置'


@app.route('/')
def index():
    return 'index.html'


class LoginView(views.MethodView):
    def get(self, error):
        return render_template('login.html', error=error)

    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")

        print(username)
        print(password)

        if username == 'test' and password == 'test':
            return '登錄成功'
        else:
            # return  render_template('login.html', error='賬號密碼錯誤')
            return self.get('賬號密碼錯誤')


class ProfileView(views.View):
    # 類視圖 裝飾器
    decorators = [login_required]

    def dispatch_request(self):
        return '個人中心'


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/profile1/', view_func=ProfileView.as_view('profile1'))

if __name__ == '__main__':
    app.run(debug=True)
