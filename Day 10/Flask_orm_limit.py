from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, ForeignKey
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


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))

    def __str__(self):
        return 'Article(id:{}, title:{})'.format(self.id, self.title)


# 模型映射到數據庫，如果存在，則不會創建
# vBase.metadata.create_all()
DB_Session = sessionmaker(bind=engine)

session = DB_Session()

# limit 限制查詢條數
# article = session.query(Article).limit(3).all()
# offset 第二個開始查三個
# article = session.query(Article).order_by(-Article.id).offset(2).limit(3).all()

# 切片
article = session.query(Article).all()[2:5]

for item in article:
    print(item)
