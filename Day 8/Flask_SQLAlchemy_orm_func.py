from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy import func

# 設定連接數據庫
HOSTNAME = "127.0.0.1"
DATABASE = "flask_demo"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

# 都要繼承這個函數生成的基類
Base = declarative_base(engine)


class User1(Base):
    __tablename__ = 'user1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(DECIMAL(20, 2), nullable=False)

    def __str__(self):
        return 'User1(id:{}, title:{}, price:{})'.format(self.id, self.title, self.price)


# 模型映射到數據庫
# Base.metadata.create_all()
#
# DB_Session = sessionmaker(bind=engine)
#
# session = DB_Session()
#
# for i in range(100):
#     user = User1(title='title{}'.format(i), price=random.randint(1, 100))
#     session.add(user)
#
# session.commit()
#
# session.close()


DB_Session = sessionmaker(bind=engine)

session = DB_Session()

users = session.query(User1).all()

# for user in users:
#     print(user.title)

"""
func.count：統計⾏的數量。
func.avg：求平均值。
func.max：求最⼤值。
func.min：求最⼩值。
func.sum：求和。
"""

result = session.query(func.count(User1.id)).all()
print(result)

result = session.query(func.avg(User1.price)).all()
print(result)

result = session.query(func.max(User1.price)).all()
print(result)

result = session.query(func.min(User1.price)).all()
print(result)

result = session.query(func.sum(User1.price)).all()
print(result)
