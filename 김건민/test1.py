from flask import Flask
import mysql_user_info
import pymysql

user = mysql_user_info.user_info
db = pymysql.connect(db=user['db'], host=user['host'], user=user['user'], passwd=user['passwd'], port=user['port'], charset=user['charset'])
#cursor = db.cursor()

app = Flask(__name__)
@app.route("/hello")
def hello():
    return "<h1>Hello Flask</h1>"

if __name__ == "__main__":
    app.run(debug = True)

#db.close()
#git test