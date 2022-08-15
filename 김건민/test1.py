from flask import Flask
from flask_cors import CORS
import mysql_user_info ## mysql 개인정보를 담은 개인 모듈
import pymysql

user = mysql_user_info.user_info

with pymysql.connect(db=user['db'], host=user['host'], user=user['user'], passwd=user['passwd'], port=user['port'],
                     charset=user['charset']) as db:
    with db.cursor(pymysql.cursors.DictCursor) as cur:
        sql = 'SELECT * FROM test'
        cur.execute(sql)
        db.commit()

        data = cur.fetchall()

app = Flask(__name__)
CORS(app)

#url
@app.route('/')
def index():

    return '<h1>%s</h1>' %data[0]['word']

# membership fee
@app.route('/fee')
def fee():
    return {
        "freshman": "15000",
        "not freshman": "10000"
    }

@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    app.run()