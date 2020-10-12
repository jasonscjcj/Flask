from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'Hello World!!! - {}'.format(request.args.get('name')) + ' Hello World!!! - {}'.format(request.form.get('name'))


# 405 Method Not Allowed
@app.route('/home2', methods=['POST'])
def home2():
    return 'Hello World!!! - {}'.format(request.args.get('name')) + ' Hello World!!! - {}'.format(request.form.get('name'))


if __name__ == '__main__':
    app.run(debug=True)
