from flask import Flask, render_template

# template_folder盡量不要修改
# app = Flask(__name__, template_folder = 'template')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('ui/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
