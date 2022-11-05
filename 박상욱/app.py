# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/fee",methods=['POST'])
def fee():
    
    req = request.get_json()

    userRes = req["userRequest"]["utterance"]	 				
    member_type = req["action"]["clientExtra"]["member_type"]	
        
    fee = 0
    
    if member_type == "재학생":
        fee = 20000
    elif member_type == "신입생":
        fee = 20000
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "동아리 회비 안내\n" + member_type + " : " + str(fee) + "원"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


@application.route("/wifi",methods=['POST'])
def wifi():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Wi-Fi name : 어서와코딩은 처음이지 (5G)\nPassword : 518interface"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

''''
@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]	 
    
    pnum = 0	
    text = ""
    
    if userRes == "????:
        # DB 
        pnum += 1
        
    elif userRes == "":
        # DB 
        pnum += -1
            
    text = ""
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }
        
    return jsonify(res)
 '''

'''
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	
    
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
'''


@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "서울특별시 광진구 능동로 209 세종대학교 학생회관 518호\nhttps://naver.me/F6mxi8mf"
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