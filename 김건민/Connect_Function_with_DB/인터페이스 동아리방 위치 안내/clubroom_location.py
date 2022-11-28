import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM location'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#[{form:'form', adress:'adress'}] 형식의 딕셔너리 리스트 형태로 data 반환
def location():
    data = _fetch()

    return data

_user = mysql_user_info.user_info

#예시
'''
from clubroom_location import *

clubroom_adress = location()

#출력예시
for dic in clubroom_adress:
    print(f'Form : {dic["type"]} | Adress : {dic["adress"]}')'''