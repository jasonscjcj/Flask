from flask import Flask, render_template, url_for, views, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('genren'))
    return '首頁'


# @app.route('/profile/')
def profile():
    return '個人中心'


class ListView(views.View):
    def dispatch_request(self):
        return '這是類視圖'


class JsonView(views.View):
    def get_response(self):
        raise NotImplementedError
    def dispatch_request(self):
        response = self.get_response()
        return jsonify(response)

class ListJsonView(JsonView):
    def get_response(self):
        return {'username': 'Jason'}

# endpoint 改掉/profile/
app.add_url_rule('/profile/', endpoint='genren', view_func=profile)
app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))
app.add_url_rule('/lists/', view_func=ListView.as_view('lists'))
app.add_url_rule('/listjson/', view_func=ListJsonView.as_view('listjson'))

if __name__ == '__main__':
    app.run(debug=True)
