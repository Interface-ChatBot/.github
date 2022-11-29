# -*- coding: utf8 -*-
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

    text = "동아리 회비 안내" + "\n" + m_type + " : " + str(club_fee) + "원"
    res = RES(text)

    return jsonify(res)


# Wi-Fi 비밀번호 안내
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



# 동아리 재실 / 퇴실 여부 체크
@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    print(req)

    #userRes = req["userRequest"]["utterance"]
    room_type = req["action"]["detailParams"]["Room_type"]["value"].encode('utf-8')	    
    print(room_type)
    pnum = 0	
    text = ""
    
    if room_type == "재실":
        # DB 
        mic_plus()
        
    elif room_type == "퇴실":
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

    res = RES(text)

    return jsonify(res)


# 동아리 재실 인원 안내
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


# 동아리방 위치 안내
@application.route("/clubroom",methods=['POST'])
def clubroom():
    '''
    data = location()

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



#동방 비번 
@application.route("/password",methods=['POST'])
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


# 인터페이스 소개
@application.route("/introduction",methods = ['POST'])
def introduction():
    req = request.get_json()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
               {
                   "listCard": {
                       "header": {
                           "title": "인터페이스를 소개합니다."
                       },
                       "items": [
                           {
                             "title":  "Interface는 프로그래밍 동아리로서, 1988년에 창설되었다."
                           },
                           {
                              "title": "동아리 자체 대회/전시회",
                               "description": "프로그래밍 전시회, 인커톤, 게임 대회",
                              "imageUrl": "http://k.kakaocdn.net/dn/Eyjyd/btrQw2OoFRH/KXZMjlfXx0ZGAM0c2msxO0/800x800.jpg"
                           },
                           {
                              "title": "다양한 스터디",
                              "description": "C언어 스터디, 파이썬 스터디, 깃허브 스터디",
                              "imageUrl":"https://blog.kakaocdn.net/dn/cShYtG/btqvQDIA107/R1K4NRACXNAUZmMdX9l2BK/img.jpg"
                           },
                           {
                               "title": "소모임 활동",
                               "description": "알고리즘 소모임, 글쓰기 소모임",
                               "imageUrl":"https://img1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/16Sg/image/LgojfD8j5dSnxveW4zzMXD_L2vY.jpg"
                           }
                           
                       ]
                   }
               }
            ]
        }
    }
    
    return jsonify(res)    



# Information on the number of people Interface members
@application.route("/people", methods = ['POST'])
def count():
    req = request.get_json()
    userRes = req["userRequest"]["utterance"]	 	
    gen_type=req["action"]["clientExtra"]["Generation_type"]
    gen_type.strip("\uae30")
    print(req)
    print('\n')
    print(userRes)
    print('\n')
    print(gen_type)

    data = generation()
    #기수별 인원수를 [{generation:기수, num:인원수}] 형식의 딕셔너리 리스트로 반환

    text = "인터페이스 " + gen_type + " : " + "명"


    res = {
        "version": "2.0",
          "template": {
            "outputs": [
              {
                "simpleText": {
                  "text": "인원 수를 알고 싶은 기수를 선택하세요.\n(30기 ~ 35기)."
                }
              }
            ],
            "quickReplies": [
              {
                "messageText": "인터페이스 30기 : 20명",
                "action": "message",
                "label": "30기"
              },
              {
                "messageText": "인터페이스 30기 : 23명",
                "action": "message",
                "label": "31기"
              },
              {
                "messageText": "인터페이스 30기 : 23명",
                "action": "message",
                "label": "32기"
              },
              {
                "messageText": "인터페이스 30기 : 36명",
                "action": "message",
                "label": "33기"
              },
              {
                "messageText": "인터페이스 30기 : 15명",
                "action": "message",
                "label": "34기"
              },
              {
                "messageText": "인터페이스 30기 : 58명",
                "action": "message",
                "label": "35기"
              }
            ]
        }
    }



    return jsonify(res)



# Interface activity schedule
@application.route("/schedule",methods = ['POST'])
def schedule():
    req = request.get_json()
    
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
        
    res = {
         "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "월을 선택해주세요"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "3월 인터페이스 일정 : " + dic["3월"],
                    "action" : "message",
                    "label" : "3월"
                },
                {
                    "messageText": "4월 인터페이스 일정 : " + dic["4월"],
                    "action" : "message",
                    "label" : "4월"
                },
                {
                    "messageText": "5월 인터페이스 일정 : " + dic["5월"],
                    "action" : "message",
                    "label" : "5월"
                },
                {
                    "messageText": "6월 인터페이스 일정 : " + dic["6월"],
                    "action" : "message",
                    "label" : "6월"
                },
                {
                    "messageText": "7월 인터페이스 일정 : " + dic["7월"],
                    "action" : "message",
                    "label" : "7월"
                },
                {
                    "messageText": "8월 인터페이스 일정 : " + dic["8월"],
                    "action" : "message",
                    "label" : "8월"
                },
                {
                    "messageText": "9월 인터페이스 일정 : " + dic["9월"],
                    "action" : "message",
                    "label" : "9월"
                },
                {
                    "messageText": "10월 인터페이스 일정 : " + dic["10월"],
                    "action" : "message",
                    "label" : "10월"
                },
                {
                    "messageText": "11월 인터페이스 일정 : " + dic["11월"],
                    "action" : "message",
                    "label" : "11월"
                },
                {
                    "messageText": "12월 인터페이스 일정 : " + dic["12월"],
                    "action" : "message",
                    "label" : "12월"
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
                        "text": "회장:류국봉 이메일:rkb429@naver.com\n 학술부장:이규리 이메일:qyul2058@gmail.com\n 학술차장:권하윤 이메일:cupertino88@naver.com\n 기획부장:이승언 이메일:banasu0723@gmail.com\n 기획차장:손재호 이메일:daymos999@gmail.comm\n 총무:임영빈 이메일:dudqlsquseo@naver.com\n 소통:동기창 이메일:tongjohn98@gmail.com\n 고문:박상욱 이메일:dkxkqkrtkddn@naver.com\n 기장:홍지섭 이메일:ghdwltjq5749@naver.com\n 부기장:공민성 이메일:gongminseong9413@gmail.com"}
                }
            ]
        }
    }
    return jsonify(res)


@application.route("/interface_link", methods=['POST'])
def interface_link():
    req = request.get_json()
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "인스타그램:https://www.instagram.com/interface518 \n 페이스북:https://www.facebook.com/interface518 \n 홈페이지:https://sejong-interface.github.io \n 깃허브: https://github.com/sejonginterface \n 메일:518interface@gmail.com \n"

                    }
                }
            ]
        }
    }
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5002, threaded=True)
