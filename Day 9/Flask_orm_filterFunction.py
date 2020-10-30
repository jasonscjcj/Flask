from sqlalchemy import create_engine, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker
import random

# 設定連接數據庫
HOSTNAME = "127.0.0.1"
DATABASE = "tablesfilter"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

# 都要繼承這個函數生成的基類
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    price = Column(DECIMAL(20, 2), nullable=False)

    def __str__(self):
        return 'Article1(id:{}, title:{}, price:{})'.format(self.id, self.title, self.price)


# 模型映射到數據庫，如果存在，則不會創建
Base.metadata.create_all(engine)

DB_Session = sessionmaker(bind=engine)

session = DB_Session()


def beginData():
    for i in range(10):
        user = User(title='title{}'.format(i), price=random.randint(1, 100))
        session.add(user)
    session.commit()
    session.close()


# eq 相等
def eqFunc(title):
    result = session.query(User).filter(User.title == title).all()
    for i in result:
        print(i)


# not eq 不相等
def noteqFunc(title):
    result = session.query(User).filter(User.title != title).all()
    for i in result:
        print(i)


# like 模糊查詢
def likeFunc(title):
    result = session.query(User).filter(User.title.like('%{}%'.format(title))).all()
    for i in result:
        print(i)


# in 在xxx裡面 [1,4]
def inFunc():
    result = session.query(User).filter(User.id.in_([1, 2])).all()
    for i in result:
        print(i)


# not in 在xxx裡面 [1,4]
def notinFunc():
    # result = session.query(User).filter(~User.id.in_([1, 2])).all()  # ~否定
    result = session.query(User).filter(User.id.notin_([1, 2])).all()  # function not in
    for i in result:
        print(i)


# is Null
# null None 不同的
# None =? 空值
# null 沒有佔位置  None為空相等於空的字符串
def notNoneFunc():
    # result = session.query(User).filter(User.title == None).all()
    result = session.query(User).filter(User.title.is_(None)).all()
    for i in result:
        print(i)


# is not null
def isNotFunc():
    # result = session.query(User).filter(User.title != None).all()
    result = session.query(User).filter(User.title.isnot(None)).all()
    for i in result:
        print(i)


# 需要import
# from sqlalchemy import and_
# and
def andFunc():
    # result = session.query(User).filter(User.title == 'title1', User.price == 4).all()
    # result = session.query(User).filter(and_(User.title == 'title1', User.price == 4)).all()
    result = session.query(User).filter(User.title == 'title1').filter(User.price == 4).all()
    for i in result:
        print(i)


# 需要import
# from sqlalchemy import or_
# Or
def orFunc():
    result = session.query(User).filter(or_(User.title == 'title1', User.price == 27)).all()
    for i in result:
        print(i)


if __name__ == '__main__':
    # beginData()
    # eqFunc("title1")
    # noteqFunc("title1")
    # likeFunc("4")
    # inFunc()
    # notinFunc()
    # notNoneFunc()
    # isNotFunc()
    # andFunc()
    orFunc()
