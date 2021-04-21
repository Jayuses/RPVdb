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

#def composedict(des,value):
#    '''将键值匹配为字典'''
#    dict = {}
#    for index,tup in enumerate(des):
#        dict[tup[0]] = value[index]
#    return dict

#def tup2dic(tup,des):
#    '''输入元组，输出对象列表'''
#    outlist = []
#    for t in tup:
#        outlist.append(composedict(des,t))
#    return outlist

#DRIVER = 'Microsoft Access Driver (*.mdb)'
#DBQ = 'C:/Users/Jayus/Desktop/RPVdb/server/instance/RPV-Simulation.mdb'
#PWD = '123456'         #密码明示，应优化
#pypyodbc.lowercase = False
#db = pypyodbc.win_connect_mdb('Driver={};DBQ={};PWD={}'.format(DRIVER,DBQ,PWD))
#cursor = db.cursor()
#idIndex = 'SPS2-专家-D-1001'
#des = [('CaseID',  0)]
#caselist = cursor.execute('SELECT CaseID,ID FROM tbCasesStruc1').fetchall()
##t = tup2dic(caselist,des)

#print(caselist)