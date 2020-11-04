from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from middleware import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# db = SQLAlchemy(app)

# user = User(name='Jason', email='jason@gmail.com', password='123')
# db.session.add(user)
# db.session.commit()

@app.route('/')
def index():
    return '這是首頁'


if __name__ == '__main__':
    app.run(debug=True)
