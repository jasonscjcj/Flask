from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # context = {
    #     'username': 'jason',
    #    'age': 18,
    #    'books': {
    #        'python': 666,
    #        'java': 777
    #    }
    # }
    # return render_template('ui/index.html', context=context)
    context = {
        'username': 'jason',
        'age': 18,
        'books': {
            'python': 666,
            'java': 777
        },
        'book': [1, 2, 3]
    }

    return render_template('ui/index.html', **context)


if __name__ == '__main__':
    app.run(debug=True, port=5004)
