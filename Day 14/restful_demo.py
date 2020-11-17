from flask import Flask
from flask_restful import Api, Resource, reqparse,inputs

app = Flask(__name__)

api = Api(app)


class IndexView(Resource):
    def get(self):
        return {
            'username': 'jason'
        }

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username', type=str, help='用戶名錯誤', required=True)
        parse.add_argument('password', type=str, help='密碼錯誤', required=True)
        parse.add_argument('age', type=int, help='年齡錯誤', required=False)
        parse.add_argument('gender', type=str, help='性別錯誤', choices=['man', 'woman'], trim=True)
        parse.add_argument('url', type=inputs.url, help='URL錯誤')
        args = parse.parse_args()
        print(args)
        return {
            'info': '登錄成功'
        }


api.add_resource(IndexView, '/', endpoint='index')

if __name__ == '__main__':
    app.run(debug=True)
