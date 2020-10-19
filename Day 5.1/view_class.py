from flask import Flask, render_template, url_for, views, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '首頁'

class BaseView(views.View):
    def __init__(self):
        self.context = {
            'username': 'jason'
        }


class LoginView(BaseView):
    def dispatch_request(self):
        return render_template('login.html', **self.context)


class RegisterView(BaseView):
    def dispatch_request(self):
        return render_template('register.html', **self.context)


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/register/', view_func=RegisterView.as_view('register'))


if __name__ == '__main__':
    app.run(debug=True)
