#!/RPVdb/server/flaskr/db.py
# -*- conding: utf-8 -*-

import pypyodbc
from flask import current_app,g

def get_db():
    '''连接数据库'''
    if 'db' not in g:
        DRIVER = 'Microsoft Access Driver (*.mdb)'
        DBQ = current_app.config['DATABASE1']
        PWD = '123456'         #密码明示，应优化
        pypyodbc.lowercase = False
        g.db = pypyodbc.win_connect_mdb('Driver={};DBQ={};PWD={}'.format(DRIVER,DBQ,PWD))
    return g.db

def get_users():
    '''连接数据库'''
    if 'users' not in g:
        DRIVER = 'Microsoft Access Driver (*.mdb)'
        DBQ = current_app.config['DATABASE2']
        PWD = '123456'         #密码明示，应优化
        pypyodbc.lowercase = False
        g.users = pypyodbc.win_connect_mdb('Driver={};DBQ={};PWD={}'.format(DRIVER,DBQ,PWD))
    return g.users

def close_db(e=None):
    db = g.pop('db', None)
    users = g.pop('users', None)

    if db is not None:
        db.close()

    if users is not None:
        users.close()

def init_app(app):
    app.teardown_appcontext(close_db)

