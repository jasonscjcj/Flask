from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    gender = Column(Integer, default=1, comment='1為男. 2為女')


# 模型映射到數據庫
Base.metadata.create_all()
