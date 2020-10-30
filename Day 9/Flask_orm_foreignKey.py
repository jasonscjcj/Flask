from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, ForeignKey
from sqlalchemy.orm import sessionmaker

HOSTNAME = "127.0.0.1"
DATABASE = "tablesfilter"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)
Base = declarative_base()


def __str__(self):
    return 'User(id:{}, name:{})'.format(self.id, self.name)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(TEXT, nullable=False)
    # uid = Column(Integer, ForeignKey(User.id))
    # 約束 RESTRICT, NO ACTION, CASCADE, SET NULL, Default = RESTRICT
    uid = Column(Integer, ForeignKey(User.id, ondelete='RESTRICT'))


# 模型映射到數據庫，如果存在，則不會創建
Base.metadata.create_all(engine)
DB_Session = sessionmaker(bind=engine)

session = DB_Session()


# user = User(name='Jason')
# session.add(user)
# session.commit()
#
# article = Article(title='Pyhone', content='xxx', uid='1')
# session.add(article)
# session.commit()

# session.close()

def deleteData():
    user = session.query(User).first()
    session.delete(user)
    session.commit()


# ForeignKey Search
def search1():
    article = session.query(Article).first()
    id = article.uid
    user = session.query(User).get(id)
    print('ID : {} - {}'.format(user.id, user.name))


def search2():
    user = session.query(User).filter(User.id == Article.uid).first()
    print('ID : {} - {}'.format(user.id, user.name))


if __name__ == '__main__':
    # deleteData()
    # search1()
    search2()