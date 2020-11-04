from flask import Flask
from flask_sqlalchemy import SQLAlchemy

HOSTNAME = "127.0.0.1"
DATABASE = "day11"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

app = Flask(__name__)

# 映射數據庫
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 不顯示警句字句

db = SQLAlchemy(app)


# 這裡可以不用自行創建表格，默認會將類名小寫化生成表格
class User(db.Model):
    # __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'User(name:{})'.format(self.name)


class Article(db.Model):
    # __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    uid = db.Column(db.Integer, db.ForeignKey('user.id')) # ondelete='CASCADE' 如刪除USER，關連SET NULL

    author = db.relationship('User', backref='articles')


db.create_all()

# 添加數據
# user = User(name='Jason')
# article = Article(title='python')
#
# article.author = user
# db.session.add(article)
# db.session.commit()

# 查詢數據
user = User.query.all()
print(user)

user1 = db.session.query(User).all()
print(user1)


# 刪除數據
# user2 = User.query.filter(User.name == 'Amy').first()
# db.session.delete(user2)
# db.session.commit()

@app.route('/')
def index():
    return '這是首頁'


if __name__ == '__main__':
    app.run(debug=True)
