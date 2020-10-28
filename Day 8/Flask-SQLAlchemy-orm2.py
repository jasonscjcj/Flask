from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Enum, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

# Integer：整形。
# Float：浮點類型。
# Boolean：傳遞True/False進去。
# DECIMAL：定點類型。
# enum：枚舉類型。
# Date：傳遞datetime.date()進去。
# DateTime：傳遞datetime.datetime()進去。
# Time：傳遞datetime.time()進去。
# String：字符類型，使⽤時需要指定⻓度，區別於Text類型。
# Text：⽂本類型。
# LONGTEXT：⻓⽂本類型。

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


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    price = Column(DECIMAL(20, 5))
    isDelete = Column(Boolean)
    gender = Column(Enum('男', '女'))
    create_at = Column(DateTime)
    content = Column(LONGTEXT)
    update_time = Column(DateTime, onupdate=datetime.now())


# 模型映射到數據庫
Base.metadata.drop_all()  # 刪除數據庫
Base.metadata.create_all()

DB_Session = sessionmaker(bind=engine)
session = DB_Session()
user = User(name='Jason', price=10.123, isDelete=False, gender='男', create_at=datetime(2020, 10, 28, 21, 38, 16),
            content='dfadfadfadfadffadfd')
session.add(user)
session.commit()

data = session.query(User).first()
data.name = 'abc'
session.commit()

session.close()

# default : 點認值 : 當你設置了default=xxx的時候，如果沒有傳這個數據，那麼數據庫會顯示你設置
# nullable : 是否可空 : nullable=False 表示不能為空
# unique : 是否唯一︰當你設置了這個參數的時候，統一列的數據不能相同，相同會報錯
# onupdate : 更新時候報行的函數
# name：該屬性在數據庫中的字段映射
# autoincrement：是否自動增長。
