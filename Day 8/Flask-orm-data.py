from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
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


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    gender = Column(Integer, default=1, comment='1為男. 2為女')


# 模型映射到數據庫，如果存在，則不會創建
Base.metadata.create_all(engine)

# 創建會話類
DB_Session = sessionmaker(bind=engine)

# 創建會話對象
session = DB_Session()

# 新增對象
article = Article(name='jason')
article1 = Article(name='jason1')
session.add(article)  # 新增一個
session.add_all([article, article1])  # 新增全部

# 如果是增刪改，需要commit
session.commit()

# 用完記得關閉
session.close()
