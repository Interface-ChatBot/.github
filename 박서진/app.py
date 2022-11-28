# -*- coding: utf8 -*-
from flask import Flask, request, jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!"

# Interface introduction
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


# Information on the number of people Interface members
@application.route("/people", methods = ['POST'])
def count():
    req = request.get_json()
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
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)