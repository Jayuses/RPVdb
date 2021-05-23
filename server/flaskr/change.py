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
        #elif style == 4:
        #    for item in del_list:
        #        for index in [1,2,3]:
        #            delete(cursor,'tbCasesStruc'+str(index),item,'SG_ID')
        #            delete(cursor,'tbStrucGeom'+str(index),item,'SG_ID')
        #elif style == 5:
        #    for item in del_list:
        #        delete(cursor,'tbCapacity',item,'Mater_ID')
        #        delete(cursor,'tbConductivity',item,'Mater_ID')
        #        delete(cursor,'tbCTE',item,'Mater_ID')
        #        delete(cursor,'tbDensity',item,'Mater_ID')
        #        delete(cursor,'tbPossion',item,'Mater_ID')
        #        delete(cursor,'tbTangent',item,'Mater_ID')
        #        delete(cursor,'tbYield',item,'Mater_ID')
        #        delete(cursor,'tbElastic',item,'Mater_ID')
        #elif style == 6:
        #    for item in del_list:
        #        for index in [1,2,3]:
        #            delete(cursor,'tbCasesStruc'+str(index),item,'LD_ID')
        #            delete(cursor,'tbLoadTP'+str(index),item,'LD_ID')
        #            delete(cursor,'tbLoadCon'+str(index),item,'LD_ID')
        cursor.commit()
        cursor.close()
    return jsonify(response_status)

def delete(cursor,table_name,index,column):
    sql = 'DELETE FROM ' + table_name + ' WHERE ' + column + '=' + "'" + index + "'"
    cursor.execute(sql)