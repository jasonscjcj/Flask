from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


# 這裡可以不用自行創建表格，默認會將類名小寫化生成表格
class AdminUser(db.Model):
    # __tablename__ = 'AdminUser'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def __repr__(self):
        return 'User(name:{})'.format(self.name)

# db.drop_all()
# db.create_all()



@app.route('/')
def index():
    return '這是首頁2'


if __name__ == '__main__':
    app.run(debug=True)
