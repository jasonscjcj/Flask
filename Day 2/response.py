from flask import Flask, Response

app = Flask(__name__)


@app.route('/abouts/')
def about():
    # return 'jason'

    # TypeError: The view function did not return a valid response.
    # The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list.
    # return [1,2,3]

    # {
    # "name": "abc",
    # "pa": "a3"
    # }
    # return {'name':'abc', 'pa': 'a3'}

    # name
    # return ('name', 'jason')

    # jason, status code
    # return 'jason', 200

    # jason text/html
    return Response('jason', status=200, mimetype='text/html')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
