import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM membership_fee'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#[{name:'name', fee:'fee'}] 형식의 딕셔너리 리스트 형식으로 동아리 회비 반환
def fee():
    data = _fetch()

    return data

_user = mysql_user_info.user_info


#예시
'''
from membership_fee import *

Fee = fee()

#출력예시
for i in Fee:
    print(f'{i["type"]} : {i["fee"]}')
'''