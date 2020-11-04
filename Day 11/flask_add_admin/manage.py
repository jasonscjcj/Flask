from flask_script import Manager
from flask_script_demo import app, AdminUser, db

# 固定寫法
manage = Manager(app)


@manage.option('-n', '--name', dest='name')
@manage.option('-e', '--email', dest='email')
def add_user(name, email, ):
    user = AdminUser(name=name, email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manage.run()
