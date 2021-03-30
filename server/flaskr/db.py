#!/RPVdb/server/flaskr/db.py
# -*- conding: utf-8 -*-

import pypyodbc
from flask import current_app,g

def get_db():
    '''连接数据库'''
    if 'db' not in g:
        DRIVER = 'Microsoft Access Driver (*.mdb)'
        DBQ = current_app.config['DATABASE']
        PWD = '123456'         #密码明示，应优化
        pypyodbc.lowercase = False
        g.db = pypyodbc.win_connect_mdb('Driver={};DBQ={};PWD={}'.format(DRIVER,DBQ,PWD))
        return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    '''在返回响应后清理时关闭数据库'''
    app.teardown_appcontext(close_db)
    SQL1 = ''