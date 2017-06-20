#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

作者：Kevin
日期：2017/6/20

"""
import pymysql
from flask import Flask, g, render_template
import chardet
from contextlib import closing

app = Flask(__name__)


def dbHandle():
    conn = pymysql.connect(
        host='45.76.79.73',
        user='root',
        db='douban',
        password='xiaoguang',
        charset='utf8',
        use_unicode=False,
    )
    return conn


# def connect_db():
#     """ connect db """
#     return sqlite3.connect(DATABASE)
#
#
# def init_db():
#     """ init db """
#     with closing(connect_db()) as db:
#         with app.open_resource('schema.sql') as f:
#             db.cursor().executescript(f.read().decode())
#         db.commit()

#
# def get_db():
#     if not hasattr(g, 'flaskr'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db


@app.route('/')
def index():
    db = dbHandle()
    cursor = db.cursor()
    cursor.execute('select * from movie')
    data = cursor.fetchall()
    print(type(data))
    print(type(str(data)))

    result = str(data).encode().decode('utf-8')
    return 'data：' + result


if __name__ == '__main__':
    # 开启调试模式
    app.run(debug=True)
