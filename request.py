#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

作者：Kevin
日期：2017/6/20

"""

from flask import request, Flask, abort, redirect, url_for

app = Flask(__name__)


@app.route('/request', methods=['GET', 'POST'])
def index():
    print(request.method)
    return redirect(url_for('login'))


@app.route('/request/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    # 这句话后不会继续执行，如果定义好了errorhandler处理则跳转过去，如果没有则显示默认页面
    abort(404)
    return '用户未登陆，请先登陆'


# 针对不同的错误码指定相应的错误页
@app.errorhandler(404)
def page_not_found(error):
    return '网页未找到'


@app.route('/request/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method == 'POST':
        result = None
        for k in request.cookies.keys():
            values = "%s=" % k + request.cookies.get(k)
            print(values)
            result = values

        return result
    else:
        return 'GET请求'


if __name__ == '__main__':
    # 开启调试模式
    app.run(debug=True)
