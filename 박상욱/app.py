# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from interface_db_edit import *

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/fee",methods=['POST'])
def _fee():
    
    req = request.get_json()

    userRes = req["userRequest"]["utterance"]	 				
    member_type = req["action"]["clientExtra"]["member_type"]	
    
    print(userRes)
    print(member_type)

    data = fee()

    club_fee = 0
    m_type = ""


    if data[0]["type"] == member_type:
        club_fee = data[0]["fee"]
        m_type = "신입생"#data[0]["type"].encoding("utf-8)
    elif data[1]["type"] == member_type:
        club_fee = data[1]["fee"]
        m_type = "재학생"#str(data[1]["type"])

    '''
    if member_type == "재학생":
        fee = 20000
    elif member_type == "신입생":
        fee = 20000
    '''

    textstr = "동아리 회비 안내" + "\n" + m_type + " : " + str(club_fee) + "원"

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": textstr
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


@application.route("/wifi",methods=['POST'])
def _wifi():
    
     data = wifi()
     str = "Wi-Fi name : "
     for i in data:
         str += i["name"] + " pw : " + i["pw"]
         str += "\n"

     res = {
         "version": "2.0",
         "template": {
             "outputs": [
                 {
                     "simpleText": {
                         #"text": "Wi-Fi name : 어서와코딩은 처음이지 (5G)\nPassword : 518interface"
                         "text": str
                     }
                 }
             ]
         }
     }
    
     return jsonify(res)

@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]	 
    
    pnum = 0	
    text = ""
    
    if userRes == "재실":
        # DB 
        mic_plus()
        
    elif userRes == "퇴실":
        DB 
        mic_minus()
            
    data = mic_show()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        #"text": text
                        "text": str(data)
                    }
                }
            ]
        }
    }
        
    return jsonify(res)

@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = mic_show()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "현재 동아리원 : " + str(pnum)
                    }
                }
            ]
        }
    }
        
    return jsonify(res)


@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    data = location()

    str = data[1]["type"] + " : " + data[1]["adress"] + "\n" + data[0]["type"] + " : " + data[0]["adress"]

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        #"text": "서울특별시 광진구 능동로 209 세종대학교 학생회관 518호\nhttps://naver.me/F6mxi8mf"
                        "text": str
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

# Interface introduction
@application.route("/introduction",methods = ['POST'])
def introduction():
    #req = request.get_json()
    
    text= "세종대학교 중앙동아리 인터페이스 연혁"
    
    #res = RES(text)
    
    return jsonify(text)

if __name__ == "__main__":
    #application.run(host='10.128.0.2', port=5000, threaded=True)
    application.run(host='0.0.0.0', port=5000, threaded=True)