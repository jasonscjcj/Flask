from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/login')
def login():
    return 'login'


@app.route('/profile/')
def profile():
    name = request.args.get('name')
    if name:
        return name
    else:
        return redirect(url_for('login'), code=301)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
