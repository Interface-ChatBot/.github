# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from interface_db import *

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
        m_type = "신입생"
        #data[0]["type"].encoding("utf-8)
    elif data[1]["type"] == member_type:
        club_fee = data[1]["fee"]
        m_type = "재학생"
        #str(data[1]["type"])

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
     str = ""
     for i in data:
         str += "name : " + i["name"] + " pw : " + i["pw"]
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
    
    #userRes = req["userRequest"]["utterance"]
    room_type = req["action"]["clientExtra"]["room_type"]	    
    print(room_type)
    pnum = 0	
    text = ""
    
    if room_type.encode('utf-8') == "재실":
        # DB 
        mic_plus()
        
    elif room_type.encode('utf-8') == "퇴실":
        # DB 
        mic_minus()
            
    data = mic_show()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        #"text": text
                        "text": "현재 동아리원 : " + str(data)
                    }
                }
            ]
        }
    }
    
    print(res)

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
		    "basicCard":  {
                        "description": "서울특별시 광진구 능동로 209 세종대학교 학생회관 518호",
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "네이버 지도 바로가기",
                                "webLinkUrl": "https://naver.me/F6mxi8mf"
                            }
                        ]
                    }   
                }
            ]
        }
    }
    
    return jsonify(res)

@application.route("/clubroom",methods=['POST'])
def password():

    #학번 이름
    #22000000 김인페
    userRes = req["userRequest"]["utterance"]

    data = member_check(userRes.split(' '))

    str = ""

    if data==1:
        str = "동아리 비밀번호 : " + "7585"
    else:
        str = "정보가 일치하지 않습니다" + "\n" + "다시 입력하거나 집부에게 문의 부탁드립니다."

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str
                    }
                }
            ]
        }
    }

#인터페이스 링크 안내
@application.route("/interface_link", methods=['POST'])
def interface_link():
    req = request.get_json()
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "인스타그램:https://www.instagram.com/interface518/"
                                "페이스북:https://www.instagram.com/interface518/"  # 인스타
                                "홈페이지:https://sejong-interface.github.io/"
                                "깃허브: https://github.com/sejonginterface"
                                "메일:518interface@gmail.com"
                    }
                }
            ]
        }
    }
    return jsonify(res)

@application.route("/executive_member", methods=['POST'])
def executive_member():
    req = request.get_json()
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "회장:류국봉 wntlghks0107@naver.com\n고문: 박상욱 dkxkqkrtkddn@naver.com\n총무:임영빈 wlso@naver.com"
                    }
                }
            ]
        }
    }
    return jsonify(res)

# Interface introduction
@application.route("/introduction",methods = ['POST'])
def introduction():
    req = request.get_json()
    
    text="인터페이스 소개\n" + "동아리 연혁 : 1988년\n"+ "주요 활동\n1. 동아리 자체 대회/ 전시회\n2. 다양한 스터디\n3. 소모임 활동"
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

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)






