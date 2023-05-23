#!/RPVdb/server/flaskr/create.py
# -*- conding: utf-8 -*-
# 蓝图文件'create.py',创建数据

import functools
from flask import (
    Blueprint, request
    )
from flaskr.db import get_db
from flask import Flask, jsonify

casedata = {'status':None}

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

@bp.route('/geom',methods=['POST','GET'])
def create_geom():
    '''在tbStrucGeom中创建结构尺寸库'''
    response_status = 0;
    if request.method == 'POST':
        geom = request.get_json()
        geomData = geom.get('newGeom')
        geomStyle = geom.get('style')
        db = get_db()
        cursor = db.cursor()
        sql1 = 'SELECT ID from tbStrucGeom'+str(geomStyle)+' WHERE SG_ID='+"'"+geomData['SG_ID']+"'"
        sql2,casedata['status'] = generate(geomStyle,geomData,'insert')
        # id = cursor.execute(sql1).fetchone()
        # if id:
        #     sql2,values = generate(geomStyle,geomData,'update')
        #     cursor.execute(sql2,values)
        # else:
        #     sql2,values = generate(geomStyle,geomData,'insert')
        #     cursor.execute(sql2,values)
        # cursor.commit()
        # casedata['status'] = 1
        # cursor.close()
    else:
        response_status = casedata['status']
    return jsonify(response_status)

            

def generate(style,geomData,mission):
    sql2 = ''
    values = []
    if mission=='update':
        sql2 = 'UPDATE tbStrucGeom'+str(style)+' SET '
        for key,value in geomData.items():
            if key == 'ID' or key == 'SG_ID':
                continue
            sql2 += (key + '=' + '?,')
            values.append(value)
        sql2 += ' WHERE SG_ID='+"'"+geomData['SG_ID']+"'"
    elif mission=='insert':
        sql2 = 'INSERT INTO tbStrucGeom'+str(style)
        column = ''
        vals = ''
        for key,value in geomData.items():
            if key == 'ID':
                continue
            column += ( key +',')
            vals += '?,'
            values.append(value)
        sql2 = sql2 + ' (' + column + ') ' +'VALUES (' + vals + ')'

    return sql2,tuple(values)

        