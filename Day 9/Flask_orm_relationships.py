from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

HOSTNAME = "127.0.0.1"
DATABASE = "tablesRelationship"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)
Base = declarative_base()




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    article = relationship('Article')
    # 添加反向查詢屬性， article 不用寫 relationship
    article = relationship('Article', backref='article')

    def __str__(self):
        return 'User(id:{}, name:{})'.format(self.id, self.name)


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(TEXT, nullable=False)
    uid = Column(Integer, ForeignKey(User.id))

    author = relationship('User')

    def __str__(self):
        return 'Article(id:{}, title:{}, content:{})'.format(self.id, self.title, self.content)


# 模型映射到數據庫，如果存在，則不會創建
Base.metadata.create_all(engine)
DB_Session = sessionmaker(bind=engine)

session = DB_Session()

# data = session.query(Article).first()
# # # print(data.uid)
# user = session.query(User).filter(Article.id == data.uid).first()
# print(user.name)
#
# data = session.query(Article).first()
# print(data.author.name)
#
# data = session.query(User).first()
# for i in data.article:
#     print(i.content)
# print(data.article)
# print(data)

user = User(name='jj')

article = Article(title='book2', content='xxxx')
article1 = Article(title='book3', content='xxxx')

article.author = user
article1.author = user

session.add(article)
session.add(article1)
session.commit()

