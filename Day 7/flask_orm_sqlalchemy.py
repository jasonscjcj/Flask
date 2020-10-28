from flask import Flask
from sqlalchemy import create_engine

# 設定連接數據庫
HOSTNAME = "127.0.0.1"
DATABASE = "flask_demo"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"

DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

with engine.connect() as conn:
    result = conn.execute("SELECT * FROM first_table")
    # print(result.fetchone()) # 拿一條數據
    print(result.fetchall()) # 拿全部數據
