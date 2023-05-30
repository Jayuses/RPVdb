#!/RPVdb/server/flaskr/change.py
# -*- conding: utf-8 -*-
# 蓝图文件'change.py',删除或更新数据

import functools
from flask import (
    Blueprint, request
    )
from flaskr.db import get_db
from flask import Flask, jsonify

status = {}

bp = Blueprint('change', __name__, url_prefix='/change')

@bp.route('/delete',methods=['POST'])
def delete():
    response_status = {'status':'fail'}
    if request.method == 'POST':
        items = request.get_json()
        style = items.get('style')
        index = items.get('index')
        db = get_db()
        cursor = db.cursor()
        if style in [1,2,3]:
            table_name = 'tbCasesStruc' + str(style)
            delete(cursor,table_name,index,'CaseID')
        elif style == 4:
            for ind in [1,2,3]:
                delete(cursor,'tbCasesStruc'+str(ind),index,'SG_ID')
                delete(cursor,'tbStrucGeom'+str(ind),index,'SG_ID')
        elif style == 5:
            delete(cursor,'tbMater',index,'MaterID')
            delete(cursor,'tbCapacity',index,'MaterID')
            delete(cursor,'tbConductivity',index,'MaterID')
            delete(cursor,'tbCTE',index,'MaterID')
            delete(cursor,'tbDensity',index,'MaterID')
            delete(cursor,'tbPossion',index,'MaterID')
            delete(cursor,'tbTangent',index,'MaterID')
            delete(cursor,'tbYield',index,'MaterID')
            delete(cursor,'tbElastic',index,'MaterID')
        elif style == 6:
            for ind in [1,2,3]:
                delete(cursor,'tbCasesStruc'+str(ind),index,'LC_ID')
                delete(cursor,'tbLoadTP'+str(ind),index,'LC_ID')
                delete(cursor,'tbLoadCon'+str(ind),index,'LC_ID')
        cursor.commit()
        cursor.close()
    return jsonify(response_status)

def delete(cursor,table_name,index,column):
    sql = 'DELETE FROM ' + table_name + ' WHERE ' + column + '=' + "'" + index + "'"
    cursor.execute(sql)