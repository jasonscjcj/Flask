from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from middleware import db
from flask_app import app

# 需要映射那個模型，就把哪個模型導入進來

manage = Manager(app)

Migrate(app, db)

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()