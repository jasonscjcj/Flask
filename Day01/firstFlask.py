#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28/4/2020 12:00:21
# @Author  : Jason Tai
# @File    : firstFlask.py
# @Software: PyCharm
# 沒有不可能的事，只有不肯做的人

from flask import Flask
from flask import request

app = Flask(__name__)

# 裝飾器 http://127.0.0.1:5000/ URL
@app.route("/")
def hello_world():
    return "hello world"

# url與函數的映射
@app.route("/jason/")
def hello_jason():
    return "這是我的第一個flask頁面"

# /list/aid
# http://127.0.0.1:5000/list/2
# int:aid = 只接收int
@app.route("/list/<int:aid>/")
def article_list(aid):
    return "這是第{}篇文章".format(aid)

# path:aid = 和string類似，但是可以傳遞斜杠/。
@app.route("/list/<path:aid>/")
def article_detail(aid):
    return "Detail-這是第{}篇文章".format(aid)

# article blog
@app.route("/<any(article, blog):url_path>/")
def item(url_path):
    return url_path

# from flask import request
# http://127.0.0.1:5000/wd?name=jason
@app.route("/wd")
def baidu():
    return request.args.get("name")

if __name__ == '__main__':

    # 1. debug mode 1 方法
    # app.debug = True
    # 2. debug mode 2 方法
    # app.run(debug=True)
    # 3. debug mode 3 方法
    # 原碼中的config file
    # app.config.update(DEBUG=True)
    # print(type(app.config))
    # print(isinstance(app.config,dict))
    # 4. debug mode 4 方法
    # 使用自定義config file，需要import config
    # app.config.from_object(config)
    # app.config.from_object('config')
    # app.config.from_pyfile('config.py', silent=True)
    # app.config.from_pyfile('config.ini', silent=True)

    app.run(debug=True)