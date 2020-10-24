from flask import Flask, url_for
from blueprints.book import book_bp
from blueprints.news import news_bp

# 子域名
# 原先 abc.com
# 子域後 cms.abc.com
from blueprints.cms import cms_bp

app = Flask(__name__)
app.register_blueprint(book_bp)
app.register_blueprint(news_bp)
app.register_blueprint(cms_bp)

app.config['SERVER_NAME'] = 'jason.com:8000'

@app.route('/')
def index():
    print(url_for('book.book_detail', bid=2))
    return '這是首頁'


if __name__ == '__main__':
    app.run(debug=True)
