#!/RPVdb/server/flaskr/search.py
# -*- conding: utf-8 -*-
# 蓝图文件'search',搜索案例

import functools
from flask import (
    Blueprint, request
    )
from flaskr.db import get_db
from flask import Flask, jsonify

casedata = {}

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/option',methods=['GET'])
def getOption():
    '''获取选项'''
    #搜索材料库
    db = get_db()
    cursor = db.cursor()
    mater = cursor.execute('SELECT MaterID FROM tbMater').fetchall()
    options1 = []
    for tup in mater:
        options1.append({
            'value':tup[0],
            'label':tup[0],
            'children':[
                {
                    'value':'弹性',
                    'label':'弹性'
                },
                {
                    'value':'弹塑性',
                    'label':'弹塑性'
                },
                ]
            })

    #搜索尺寸库和工况库
    options2 = []
    options3 = []
    idlist2 = [] #辅助列表
    idlist3 = []
    for index in range(3):
        table1 = 'tbStrucGeom'+str(index+1)
        table2 = 'tbLoadCon'+str(index+1)
        sql1 = "SELECT SG_ID FROM " + table1
        sql2 = "SELECT LC_ID FROM " + table2
        geomlist = cursor.execute(sql1).fetchall()
        loadlist = cursor.execute(sql2).fetchall()
        for li in geomlist:
            if li[0] not in idlist2:
                options2.append({'value':li[0],'label':li[0]})
                idlist2.append(li[0])
            else:
                continue;
        for li in loadlist:
            if li[0] not in idlist3:
                options3.append({'value':li[0],'label':li[0]})
                idlist3.append(li[0])
            else:
                continue;
    options = {
        'mater':options1,
        'geom':options2,
        'load':options3
        }
    cursor.close()
    return jsonify(options)

@bp.route('/find',methods=['GET','POST'])
def findCase():
    '''搜索算例'''
    response_list = []
    if request.method == 'POST':
        case = request.get_json()
        db = get_db()
        cursor = db.cursor()
        outlist = []
        style = case.get('style')
        if style:
            sql = get_sql(case,style)
            caselist = cursor.execute(sql).fetchall()
            for tup in caselist:
                outlist.append({'CaseID':tup[0],'style':style})
            casedata['list'] = outlist
            cursor.close()
        else:
            for style in [1,2,3]:
                sql = get_sql(case,style)
                caselist = cursor.execute(sql).fetchall()
                for tup in caselist:
                    outlist.append({'CaseID':tup[0],'style':style})
            casedata['list'] = outlist
            cursor.close()
    else:
        response_list = casedata['list']
    return jsonify(response_list)

def get_sql(case,style):
    sql = 'SELECT CaseID FROM tbCasesStruc'+str(style)
    SG_ID = case.get('SG_ID')
    LC_ID = case.get('LC_ID')
    MHead = case.get('MHead')
    MRPV = case.get('MRPV')
    MBolt = case.get('MBolt')
    MLayer = case.get('MLayer')
    if SG_ID:
        sql = sql + ' WHERE SG_ID=' + "'" +SG_ID + "'"
    if LC_ID:
        if sql[-6:-1] == 'Struc':
            sql = sql + ' WHERE LC_ID=' + "'" + LC_ID + "'"
        else:
            sql = sql + ' AND LC_ID=' + "'" + LC_ID + "'"
    if MHead:
        if sql[-6:-1] == 'Struc':
            sql = sql + ' WHERE MHead=' + "'" + MHead[0] + "'" + ' AND MHeadAM=' + "'" + MHead[1] + "'"
        else:
            sql = sql + ' AND MHead=' + "'" + MHead[0] + "'" + ' AND MHeadAM=' + "'" + MHead[1] + "'" 
    if MRPV:
        if sql[-6:-1] == 'Struc':
            sql = sql + ' WHERE MRPV=' + "'" + MRPV[0] + "'" + ' AND MRPVAM=' + "'" + MRPV[1] + "'"
        else:
            sql = sql + ' AND MRPV=' + "'" + MRPV[0] + "'" + ' AND MRPVAM=' + "'" + MRPV[1] + "'"
    if MBolt:
        if sql[-6:-1] == 'Struc':
            sql = sql + ' WHERE MBolt=' + "'" + MBolt[0] + "'" + ' AND MBoltAM=' + "'" + MBolt[1] + "'"
        else:
            sql = sql + ' AND MBolt=' + "'" + MBolt[0] + "'" + ' AND MBoltAM=' + "'" + MBolt[1] + "'"
    if MLayer:
        if sql[-6:-1] == 'Struc':
            sql = sql + ' WHERE MLayer=' + "'" + MLayer[0] + "'" + ' AND MLayerAM=' + "'" + MLayer[1] + "'"
        else:
            sql = sql + ' AND MLayer=' + "'" + MLayer[0] + "'" + ' AND MLayerAM=' + "'" + MLayer[1] + "'"
    return sql
