from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'username': 'Jason',
        'age': -18,
        'home': 'Hong Kong',
        'name': 'logic',
        'es': "<script>alert('hello');</script>",  # escape
        'books': ['Python', 'Java', 'PHP'],
        'book': {'Python': 666},
        'tc': 'Hello Jason',
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
