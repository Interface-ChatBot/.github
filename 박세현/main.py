# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from interface_db import *
from res import RES


application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!" #구름 서버 사용


# 동아리 회비 안내
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

    text = "동아리 회비 안내" + "\n" + m_type + " : " + str(club_fee) + "원"
    res = RES(text)

    return jsonify(res)


# Wi-Fi 비밀번호 안내
@application.route("/wifi",methods=['POST'])
def wifi():

    req = request.get_json()
    
    text = "Wi-Fi name : 어서와코딩은처음이지 (5G)\nPassword : 518interface"
    
    res = RES(text)
    
    
    return jsonify(res)

'''
//다른 와이파이 방식인데, 이것도 굳이 데베에서 불러와야하나.
@application.route("/wifi",methods=['POST'])
def _wifi():
    
    data = wifi()
    str = ""
    for i in data:
        str += "name : " + i["name"] + " pw : " + i["pw"]
        str += "\n"

    text=str
    res = RES(text)

    return jsonify(res)

'''


# 동아리 재실 / 퇴실 여부 체크
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

    res = RES(text)

    return jsonify(res)


# 동아리 재실 인원 안내
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	# DB에서 값 가져오기
    
    text="현재 동아리방 재실 인원 : " + str(pnum)
    
    res = RES(text)
        
    return jsonify(res)



#현재 동아리 인원
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
        
    res = RES(text)

    return jsonify(res)



# 동아리방 위치 안내
@application.route("/clubroom",methods=['POST'])
def clubroom():
    '''
    data = location()// 굳이 불러와야 하나..?

    str = data[1]["type"] + " : " + data[1]["adress"] + "\n" + data[0]["type"] + " : " + data[0]["adress"]
    '''
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


'''
#동방 비번 (주소 바꿔야함. 겹침.)
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

    res = RES(str)

    return jsonify(res)
'''

# 인터페이스 소개
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
    print(req)
    
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
    print(req)
    
    userRes = req["userRequest"]["utterance"]
    Generation_type = req["action"]["clientExtra"]["Generation_type"]
    
    dic_gen = {30 : 20, 31 : 23, 32 : 23, 33 : 36, 34 : 15, 35 : 58}
    
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
    print(req)

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard":{
                        "title" : "인터페이스 건의사항",
                        "thumbnail":{
                            "imageUrl":"https://~~"
                        },
                        "button": [
                            {    
                                "action": "webLink",
                                "label" : "구글폼 링크",
                                "webLinkUrl":"https://~~"
                            }
                        ]
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


#인터페이스 집부 구성원 안내
@application.route("/executive_member", methods=['POST'])
def executive_member():
    req = request.get_json()
    text="회장:류국봉 wntlghks0107@naver.com\n고문: 박상욱 dkxkqkrtkddn@naver.com\n총무:임영빈 wlso@naver.com"
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
    application.run(host='0.0.0.0', port=5002, threaded=True)
