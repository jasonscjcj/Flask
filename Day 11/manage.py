from flask_script_demo import Manager
from flask_sqlalchemy_plugin import app


# 固定寫法
manage = Manager(app)


@manage.command
def index():
    return 'hello python'


@manage.option('-n', '--name', dest='name')
@manage.option('-u', '--url', dest='url')
def hello(name, url):
    print("hello", name, url)


if __name__ == '__main__':
    manage.run()
