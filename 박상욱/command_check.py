# -*- coding: utf-8 -*-
from command_analyze import *
import pymysql
import mysql_user_info

#데이터베이스에서 데이터 가져오기
def _fetch(table):
    db = pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset'])
    cur = db.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM ' + table
    cur.execute(sql)
    db.commit()

    data = cur.fetchall()
    db.close()

    return data

#매개변수 user_input에 대한 유사도 검증 후 {'단어' : 유사율}의 딕셔너리 형태로 0.5 이상 유사한 단어 반환, 0.5 유사율을 충족시키는 단어가 없을 경우 'None' 반환
def command(user_input):
    result = {}
    for dic in _data:
        example = dic['example']

        if len(user_input) < len(dic["example"]):
            a = user_input
            b = example
        else:
            b = user_input
            a = example

        if check(b):
            a1 = ngram(s_list(b), 1)
            #print(a1)

            b1 = ngram(s_list(a), 1)
            #print(b1)

            #print(similarity(a1, b1))
            if similarity(a1, b1) >= 0.5:
                '''print(f"'{b}'과(와) '{a}'가(이) 유사함")'''

                try:
                    if result[dic["command"]] < similarity(a1, b1):
                        result[dic["command"]] = similarity(a1, b1)
                except:
                    result[dic["command"]] = similarity(a1, b1)
            '''else:
                print(f"'{b}'과(와) '{a}'가(이) 유사하지 않음")'''

        else:
            cnt = 0

            a1 = ngram(s_list(b), 1)
            #print(a1)
            b1 = ngram(s_list(a), 1)
            #print(b1)

            a2 = ngram(n_list(b), 1)
            a3 = ngram(m_list(b), 1)

            b2 = ngram(n_list(a), 1)
            b3 = ngram(m_list(a), 1)

            if (similarity(a2, b2) >= 0.5):
                cnt += 0.1
            if (similarity(a3, b3) >= 0.5):
                cnt += 0.1

            #print(similarity(a1, b1) + cnt)
            if (similarity(a1, b1) + cnt >= 0.5):
                '''print(f"'{b}'과(와) '{a}'가(이) 유사합니다.")'''
                try:
                    if result[dic["command"]] < similarity(a1, b1) + cnt:
                        result[dic["command"]] = similarity(a1, b1) + cnt
                except:
                    result[dic["command"]] = similarity(a1, b1) + cnt
            '''else:
                print(f"'{b}'과(와) '{a}'가(이) 유사하지 않습니다.")'''

        '''print('-' * 100)'''

    if len(result) != 0:
        return result
    else:
        return 'None'

_user = mysql_user_info.user_info
_data = _fetch('command')

if __name__ == "__main__":
    print(command(input()))

#예시
'''
from command_check import *

user_input = input()
result = command(user_input)
'''