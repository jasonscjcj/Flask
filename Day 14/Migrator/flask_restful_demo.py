from flask import Flask
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal, marshal_with
import config
from middleware import db
from models import Article

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

api = Api(app)


class ArticleView(Resource):
    resource_fields = {
        'article_title': fields.String(attribute='title'),
        'content': fields.String,
        # 'author':fields.String,  #     "author": "<User 1>",
        # 'tags':fields.String     #     "tags": "[<Tag 1>]"
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String
        }),
        'tags': fields.List(
           fields.Nested({
              'id': fields.Integer,
               'name':fields.String
           })
        ),
        'read_count':fields.Integer(default=0)
    }

    # {
    #     "title": "python",
    #     "content": "xxxxx",


    # }

    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article


class IndexView(Resource):
    def get(self):
        return 'Index Page'


api.add_resource(ArticleView, '/article/<article_id>', endpoint='article')
api.add_resource(IndexView, '/', endpoint='index')

if __name__ == '__main__':
    app.run(debug=True)
