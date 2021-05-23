#!/RPVdb/server/flaskr/create.py
# -*- conding: utf-8 -*-
# 蓝图文件'create.py',创建数据

import functools
from flask import (
    Blueprint, request
    )
from flaskr.db import get_db
from flask import Flask, jsonify

casedata = {}

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route('/case',methods=['POST','GET'])
def create_case():
    '''在创建tbCaseStrucX中创建案例'''
    response_status = 0;
    if request.method == 'POST':
        case = request.get_json()
        CaseID = case.get('CaseID')
        caseinfo = case.get('caseinfo')
        db = get_db()
        cursor = db.cursor()
        sql1 = 'SELECT ID from tbCasesStruc'+str(caseinfo['style'])+' WHERE CaseID='+"'"+CaseID+"'"
        id = cursor.execute(sql1).fetchone()
        if id:
            casedata['status'] = 2
        else:
            sql2 = 'INSERT INTO tbCasesStruc'+str(caseinfo['style'])+\
                ' (CaseID,SG_ID,LC_ID,MHead,MHeadAM,MRPV,MRPVAM,MBolt,MBoltAM,MLayer,MLayerAM)'+\
                'VALUES (?,?,?,?,?,?,?,?,?,?,?)'
            cursor.execute(sql2,(CaseID,caseinfo['SG_ID'],caseinfo['LC_ID'],
                                 caseinfo['MHead'][0],caseinfo['MHead'][1],
                                 caseinfo['MRPV'][0],caseinfo['MRPV'][1],
                                 caseinfo['MBolt'][0],caseinfo['MBolt'][1],
                                 caseinfo['MLayer'][0],caseinfo['MLayer'][1]))
            cursor.commit()
            casedata['status'] = 1
        cursor.close()
    else:
        response_status = casedata['status']
    return jsonify(response_status)
        