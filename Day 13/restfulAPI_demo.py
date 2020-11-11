from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

# 用Api來綁定app
api = Api(app)


class IndexView(Resource):
    def get(self):
        return {'username': 'Jason'}

    def post(self):
        return {'username': 'Jasonp'}

api.add_resource(IndexView, '/', endpoint='index')

if __name__ == '__main__':
    app.run(debug=True)
