from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

HOSTNAME = "127.0.0.1"
DATABASE = "table_One_To_One"
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
    password = Column(String(100))
    # uselist = One To One Relationship
    address = relationship("Address", backref='address', uselist=False)

    def __str__(self):
        return 'User(id:{}, name:{})'.format(self.id, self.name)


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __str__(self):
        return 'Article(id:{}, title:{}, content:{})'.format(self.id, self.title, self.content)


# 模型映射到數據庫，如果存在，則不會創建
# Base.metadata.create_all()
DB_Session = sessionmaker(bind=engine)

session = DB_Session()

user = User(name='Jason', password='123')
address = Address(email_address='xxx@xxx.com')
address1 = Address(email_address='yyy@yyy.com')

user.address = address
user.address = address1
session.add(user)
session.commit()
session.close()
