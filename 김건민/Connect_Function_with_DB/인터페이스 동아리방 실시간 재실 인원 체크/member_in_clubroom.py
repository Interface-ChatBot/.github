import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM member_in_clubroom'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#현 인원수 int형으로 return
def mic_show():
    data = _fetch()

    return data[0]['num_of_member']

#현 인원수 데이터 1 증가
def mic_plus():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'],
                         charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'UPDATE member_in_clubroom SET num_of_member = num_of_member + 1'
            cur.execute(sql)
            db.commit()

#현 인원수 데이터 1 감소
#but 현 인워수가 0명인 경우 아무것도 하지 안음
def mic_minus():
    data = _fetch()

    if data[0]['num_of_member'] == 0:
        return 0

    else:
        with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'],
                             charset=_user['charset']) as db:
            with db.cursor(pymysql.cursors.DictCursor) as cur:
                sql = 'UPDATE member_in_clubroom SET num_of_member = num_of_member - 1'
                cur.execute(sql)
                db.commit()

#현 인원수 데이터를 0으로 초기화
def mic_init():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'],
                         charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'UPDATE member_in_clubroom SET num_of_member = 0'
            cur.execute(sql)
            db.commit()

_user = mysql_user_info.user_info

#예시
'''
from member_in_clubroom import *

cmd = input()

if cmd == 'show':
    num = mic_show()
    print(f'{num}명')

elif cmd == 'plus':
    mic_plus()

elif cmd == 'minus':
    mic_minus()

elif cmd == 'init':
    mic_init()
'''