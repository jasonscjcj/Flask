#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28/4/2020 15:16:39
# @Author  : Jason Tai
# @File    : url_demo.py
# @Software: PyCharm
# 沒有不可能的事，只有不肯做的人

from flask import Flask, url_for,request

app = Flask(__name__)

@app.route("/")
def index():
    # /article/2/ 只傳一個參數aid
    # 根據函數的名字，進行反轉，得到函數對應的路由 重定向
    print(url_for("article_list",aid=2))
    return "index Page"

# http://127.0.0.1:5000/article/2/
@app.route("/article/<aid>/")
def article_list(aid):
    return "article list {}".format(aid)

@app.route("/detail/<did>/")
def article_detail(did):
    print(url_for("index"))
    # 沒有參數要傳時，有參數傳入會變為查詢
    # /?next=123
    print(url_for("index", next="123"))
    return "article detail {}".format(did)

# 指定HTTP請求方法
# 默認都是接受GET請求
@app.route("/login/", methods=['POST'])
def login():
    # GET 參數直接在URL中
    # POST 參數沒有直接體現在URL地址中
    # import request
    # print(type(request.args))
    # GET請求接受參數
    # print(request.args.get('username'))
    # POST 請求接受參數
    print(request.form.get("name"))

    return "login"
if __name__ == '__main__':
    app.run(debug=True)