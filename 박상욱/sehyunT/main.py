# -*- coding: utf8 -*-

from flask import Flask, request, jsonify
from res import RES

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!" #구름 서버 사용



# 동아리 회비 안내
@application.route("/fee",methods=['POST'])
def fee():
    # 신입생인지 재학생인지 request로 구분
    
    req = request.get_json()

    
    userRes = req["userRequest"]["utterance"]	 				#사용자 발화 저장
    member_type = req["action"]["clientExtra"]["member_type"]	#바로가기 parameter 저장
        
    fee = 0
    
    if member_type == "신입생":
        fee = 20000
    elif member_type == "재학생":
        fee = 20000
    
    text = "[동아리 회비]\n" + member_type + " : " + str(fee) + "원"
    
    res = RES(text)
    
    return jsonify(res)

# Wi-Fi 비밀번호 안내
@application.route("/wifi",methods=['POST'])
def wifi():

    req = request.get_json()
    
    text = "Wi-Fi name : 어서와코딩은처음이지 (5G)\nPassword : 518interface"
    
    res = RES(text)
    
    
    return jsonify(res)


# 동아리 재실 / 퇴실 여부 체크
@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]	 #사용자 발화 저장
    
    pnum = 0	#DB에서 가져오기
    text = ""
    
    if userRes == "재실":
        # DB 재실인원 증가
        pnum += 1
        
    elif userRes == "퇴실":
        # DB 재실인원 감소
        pnum += -1
            
    text = "현재 재실 인원은 " + str(pnum) + "명 입니다."
    
    # 6시에 재실인원 0으로 초기화
    
    
    res = RES(text)
        
    return jsonify(res)


# 동아리 재실 인원 안내
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	# DB에서 값 가져오기
    
    text="현재 동아리방 재실 인원 : " + str(pnum)
    
    res = RES(text)
        
    return jsonify(res)



# 동아리방 위치 안내
@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    text = "동아리방 위치 : 세종대학교 학생회관 518호\nhttps://naver.me/F6mxi8mf"
    
    res = RES(text)
    
    return jsonify(res)


# Interface introduction
@application.route("/introduction",methods = ['POST'])
def introduction():
    req = request.get_json()
    
    text="인터페이스 소개\n" + "동아리 연혁 : 1988년\n"+ "주요 활동\n1. 동아리 자체 대회/ 전시회\n2. 다양한 스터디\n3. 소모임 활동"
    res = RES(text)
    
    return jsonify(res)
    

# Interface activity schedule
@application.route("/schedule",methods = ['POST'])
def schedule():
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]
    Month_type = req["action"]["clientExtra"]["Month_type"]
    
    dic = {"3월" : "1학기 개강총회, 신입생 환영회, 봄엠티", 
           "4월" : "스터디, 소모임",
           "5월" : "기엠티",
           "6월" : "게임 대회",
           "7월" : "1학기 종강총회",
           "8월" : "여름엠티 or 가을 엠티",
           "9월" : "2학기 개강총회",
           "10월" : "기타 행사(게임 대회, 상영 행사)",
           "11월" : "창립제",
           "12월" : "프로그래밍 전시회, 2학기 종강 총회"
          }
    
    if Month_type == "3월":
        schedule = dic["3월"]
    elif Month_type == "4월":
        schedule = dic["4월"]
    elif Month_type == "5월":
        schedule = dic["5월"]
    elif Month_type == "6월":
        schedule = dic["6월"]
    elif Month_type == "7월":
        schedule = dic["7월"]
    elif Month_type == "8월":
        schedule = dic["8월"]
    elif Month_type == "9월":
        schedule = dic["9월"]
    elif Month_type == "10월":
        schedule = dic["10월"]
    elif Month_type == "11월":
        schedule = dic["11월"]
    elif Month_type == "12월":
        schedule = dic["12월"]

    text=Month_type + " 동아리 일정 안내\n" + schedule
        
    res = RES(text)

    return jsonify(res)


# Information on the number of people Interface members
@application.route("/people",methods = ['POST'])
def people():
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]
    Generation_type = req["action"]["clientExtra"]["Generation_type"]
    
    dic_gen = {30 : 10, 31 : 20, 32 : 34, 33 : 45, 34 : 50, 35 : 70}
    
    if Generation_type == "30기":
        people = dic_gen[30]
    elif Generation_type == "31기":
        people = dic_gen[31]
    elif Generation_type == "32기":
        people = dic_gen[32]
    elif Generation_type == "33기":
        people = dic_gen[33]
    elif Generation_type == "34기":
        people = dic_gen[34]
    elif Generation_type == "35기":
        people = dic_gen[35]

    text = "인터페이스 " + Generation_type + " : " + str(people) + "명"
    res = RES(text)
    
    return jsonify(res)


# Interface suggestion
@application.route("/suggestion",methods = ['POST'])
def suggestion():
    req = request.get_json()

    text = ""
    res = RES(text)
    
    return jsonify(res)

#인터페이스 집부 구성원 안내
@application.route("/executive_member", methods=['POST'])
def executive_member():
    req = request.get_json()

    text = "회장:아무개 wntlghks0107@naver.com\n부회장:이무개 wntis0107@naver.com\n총무:길동 wlso@naver.com"

    res = RES(text)
    
    return jsonify(res)

#인터페이스 링크 안내
@application.route("/interface_link", methods=['POST'])
def interface_link():
    req = request.get_json()

    text = {"인스타그램:https://www.instagram.com/interface518/"
            "페이스북:https://www.instagram.com/interface518/"  # 인스타
            "홈페이지:https://sejong-interface.github.io/"
            "깃허브: https://github.com/sejonginterface"
            "메일:518interface@gmail.com"}

    res = RES(text)

    return jsonify(res)

#인터페이스 행사 소개
@application.route("/event", methods=['POST'])
def event():
    req = request.get_json()
    image=req['action']['params']['event']

    print(image)
    res={"version":"2.0",
         "template":{"outputs":[{
             "listCard":{
                 "header":{
                     "title":"인터페이스 행사"
                 },
                 "items":[
                     {
                         "title":"인프전",
                         "description":"인터페이스 프로그래밍 전시회",
                         "imageUrl":"https//~~~",
                         "link":{
                             "web":"https//~~"
                         }
                     },
                     {
                         "title": "인커톤",
                         "description": "인터페이스 자체 해커톤",
                         "imageUrl": "https//~~~",
                         "link": {
                             "web": "https//~~"
                         }
                     },
                     {
                         "title": "스터디",
                         "description": "더 공부하고 싶은 학생을 위한 스터디!",
                         "imageUrl": "https//~~~",
                         "link": {
                             "web": "https//~~"
                         }
                     },
                 ],
                 "button":[
                     {
                         "label":"깃허브 링크",
                         "action":"weblink",
                         "weblinkUrl":"https://github.com/sejonginterface"
                     }
                 ]
             }
         }

         ]}}
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5004, threaded=True)
