from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

# 設定連接數據庫
HOSTNAME = "127.0.0.1"
DATABASE = "flask_demo"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

# 都要繼承這個函數生成的基類
Base = declarative_base()


class Article1(Base):
    __tablename__ = 'article1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    content = Column(String(50))
    author = Column(String(50))

    def __str__(self):
        return 'Article1(name:{}, content:{}, author:{})'.format(self.name, self.content, self.author)


# 模型映射到數據庫，如果存在，則不會創建
Base.metadata.create_all(engine)

DB_Session = sessionmaker(bind=engine)

session = DB_Session()


# 增加數據
def add_data():
    article = Article1(name='Python', content='人生苦短，我用Python', author='龜叔')
    session.add(article)
    session.commit()


# 查詢數據
def search_all_data():
    # 查詢所有
    data = session.query(Article1).all()
    # 麻煩方法
    # for item in data:
    #     print(item.name)
    #     print(item.content)
    #     print(item.author)
    # 麻煩方法

    # call __str__
    for item in data:
        print(item)


def search_filter_data():
    data = session.query(Article1).filter(Article1.name == 'Python').all()
    for item in data:
        print(item)


# 用filter_by = xxx
def search_filterBy_data():
    data = session.query(Article1).filter_by(name='Python').all()
    for item in data:
        print(item)


# 查第一條數據
def search_one_data():
    data = session.query(Article1).first()
    print(data)


# 查第幾條數據
def search_index_data():
    data = session.query(Article1).get(2)  # 查不到的話 = None
    print(data)


# 更新
def update_data():
    data = session.query(Article1).first()
    data.name = 'logic'
    print(data.name)
    session.commit()
    # session.rollback()


# 刪除 TODO
def delete_data():
    data = session.query(Article1).first()
    result = session.query(Article1).filter_by(id=data.id).first()
    result.isDelete = True
    session.commit()


# 新加Column
def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


if __name__ == '__main__':
    # Alter Table
    # column = Column('isDetele', Boolean, default=False)
    # add_column(engine, 'article1', column)

    # add_data()
    # search_all_data()
    # search_filter_data()
    # search_filterBy_data()
    # search_one_data()
    # search_index_data()
    # update_data()
    delete_data()
