from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table

HOSTNAME = "127.0.0.1"
DATABASE = "table_Many_To_Many"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)
Base = declarative_base(engine)

# 創建中間表格的定義，就是為了保存著兩個表的外鍵
# my_table = Table('mytable', metadata,
#         ...                 Column('id', Integer, primary_key=True),
#         ...                 Column('version_id', Integer, primary_key=True),
#         ...                 Column('data', String(50))
teacher_classes = Table(
    'teacher_classes',
    Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teacher.id')),
    Column('classes_id', Integer, ForeignKey('classes.id'))
)


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    # Many to Many "Secondary"
    classes = relationship('Classes', backref='teachers', secondary=teacher_classes)

    def __str__(self):
        return 'Teacher(id:{}, name:{})'.format(self.id, self.name)


class Classes(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __str__(self):
        return 'Classes(id:{}, name:{})'.format(self.id, self.name)


# 模型映射到數據庫，如果存在，則不會創建
# Base.metadata.create_all()
DB_Session = sessionmaker(bind=engine)

session = DB_Session()

# 加數據
teacher1 = Teacher(name='Jason')
teacher2 = Teacher(name='amy')

classes1 = Classes(name='Python Classes')
classes2 = Classes(name='Java Classes')

# teacher1.classes.append(classes1, classes2) # error
teacher1.classes.append(classes1)
teacher1.classes.append(classes2)

# teacher2.classes.append(classes1, classes2) # error
teacher2.classes.append(classes1)
teacher2.classes.append(classes2)
session.add(teacher1)
session.add(teacher2)
session.commit()
session.close()

# 查詢檢證表是否正確
# 根據老師查班級
teacher = session.query(Teacher).first()
# print(teacher)
for item in teacher.classes:
    print(item)

# 根據班級查老師
classes = session.query(Classes).first()
# print(classes)
for item in classes.teachers:
    print(item)
