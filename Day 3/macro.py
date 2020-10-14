from flask import Flask, render_template

app = Flask(__name__)
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

@app.route('/')
def macro():
    return render_template('macro.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
