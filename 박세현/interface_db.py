# -*- coding: utf8 -*-
import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch(table):
    db =  pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset'])
    cur = db.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM ' + table
    cur.execute(sql)
    db.commit()

    data = cur.fetchall()
    db.close()

    return data

###wifi

#[{name:'name', pw:'pw'}] 형식의 딕셔너리 리스트 형식으로 wifi 비밀번호 반환
def wifi():
    data = _fetch('wifi')

    return data

###member_check

#이름, 학번을 [학번 이름] 리스트 형식으로 member_check 함수에 넣었을 경우 DB 안에 있는 데이터 중 이름과 학번이 정확하게 일치하면 1을 반환, 아닐시 0을 반환
def member_check(user_input):
    data = _fetch('member')

    c = 0
    for i in data:
        if i['name'] == user_input[0] and i['id'] == int(user_input[1]):
            c = 1
            break

    return c

###member_in_clubroom

#현 인원수 int형으로 return
def mic_show():
    data = _fetch('member_in_clubroom')

    return data[0]['num_of_member']

#현 인원수 데이터 1 증가
def mic_plus():
    db = pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'],
                         charset=_user['charset'])
    cur = db.cursor(pymysql.cursors.DictCursor)
    sql = 'UPDATE member_in_clubroom SET num_of_member = num_of_member + 1'
    cur.execute(sql)
    db.commit()
    db.close()

#현 인원수 데이터 1 감소
#but 현 인워수가 0명인 경우 아무것도 하지 안음
def mic_minus():
    data = _fetch('member_in_clubroom')

    if data[0]['num_of_member'] == 0:
        return 0

    else:
        db = pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'],
                             charset=_user['charset'])
        cur = db.cursor(pymysql.cursors.DictCursor)
        sql = 'UPDATE member_in_clubroom SET num_of_member = num_of_member - 1'
        cur.execute(sql)
        db.commit()
        db.close()

#현 인원수 데이터를 0으로 초기화
def mic_init():
    db = pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'],
                         charset=_user['charset'])
    cur = db.cursor(pymysql.cursors.DictCursor)
    sql = 'UPDATE member_in_clubroom SET num_of_member = 0'
    cur.execute(sql)
    db.commit()
    db.close()

###clubroom_location

#[{form:'form', adress:'adress'}] 형식의 딕셔너리 리스트 형태로 data 반환
def location():
    data = _fetch('location')

    return data

###membership_fee

#[{name:'name', fee:'fee'}] 형식의 딕셔너리 리스트 형식으로 동아리 회비 반환
def fee():
    data = _fetch('membership_fee')

    return data

###executives

#임원진 정보를 [{name:'name', position:'position', email:'email'}] 형식의 딕셔너리 리스트로 반환
def executives():
    data = _fetch('executives')

    return data

###link

#사이트 정보를 [{site:'site', link:'link"}] 형식의 딕셔너리 리스트로 반환
def link():
    data = _fetch('connect')

    return data

_user = mysql_user_info.user_info

## generation_of_member

#기수별 인원수를 [{generation:기수, num:인원수}] 형식의 딕셔너리 리스트로 반환
def generation():
    data = _fetch('generation')

    return data

## 사용 예시
'''
from interface_db import *
'''