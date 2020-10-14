from flask import Flask, render_template

app = Flask(__name__)

context = {
    'username': 'Jasossn',
    'age': 18,
    'books': ['Python', 'Java', 'PHP'],
    'book': {'Python': 666, 'Java': 777, 'PHP': 888}
}


@app.route('/')
def if_for():
    return render_template('if_for.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
