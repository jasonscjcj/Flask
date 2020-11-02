from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table

HOSTNAME = "127.0.0.1"
DATABASE = "orderFilter"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    gender = Column(Enum('男', '女'))
    age = Column(Integer)

    def __str__(self):
        return 'Article(id:{}, name:{}, gender:{}, age:{})'.format(self.id, self.name, self.gender, self.age)


# 模型映射到數據庫，如果存在，則不會創建
# Base.metadata.create_all()
DB_Session = sessionmaker(bind=engine)

session = DB_Session()

import random

# for i in range(10):
#     user = User(name='U%s' % i, gender='男', age=random.randint(10, 25))
#     session.add(user)
#
# session.commit()
# session.close()

# group_by
# 通過和聚合函數組合一起使用
from sqlalchemy import func
# 男女分組
result = session.query(User.gender, func.count(User.id)).group_by(User.gender).all()
# 年齡分組
result = session.query(User.age, func.count(User.age)).group_by(User.age).all()
# session.query(User.age, func.count(User.age)) 原始查詢結果
result = session.query(User.age, func.count(User.age)).group_by(User.age).having(User.age < 18).all()

# 兩條數據子查詢
user = session.query(User).filter(User.name == 'U1').first()
# print(user)
data = session.query(User).filter(User.gender == user.gender, User.age == user.age).all()
for item in data:
    print(item)

# 子查詢
sub = session.query(User.gender.label('gender'), User.age.label('age')).filter(User.name == 'U1').subquery()
data = session.query(User).filter(User.gender == sub.c.gender, User.age == sub.c.age).all()
for item in data:
    print(item)