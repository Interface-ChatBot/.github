import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM connect'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#사이트 정보를 [{site:'site', link:'link"}] 형식의 딕셔너리 리스트로 반환
def link():
    data = _fetch()

    return data

_user = mysql_user_info.user_info

'''
from link import *

link = link()

#출력예시
for l in link:
    print(f'Site : {l["site"]} | connect : {l["link"]}')'''