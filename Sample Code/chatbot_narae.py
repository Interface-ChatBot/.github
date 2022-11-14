# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify

chatbot_narae = Flask(__name__)


@chatbot_narae.route("/")
def start():
    return "Hello goorm!"


# 화성시장학관 동작나래관 사생용 챗봇 스킬

# 식사 시간
@chatbot_narae.route("/Meal_Time",methods=['POST'])
def Meal_Time():
    
    textstr = "화성시장학관 동작나래관의 식사시간 입니다.\n\n"
    textstr += "평일\n"
    textstr += "아침: 7:00-8:30\n"
    textstr += "점심: 11:40-13:00\n"
    textstr += "저녁: 18:00-19:30\n"
    textstr += "주말\n"
    textstr += "아침: 8:00-9:00\n"
    textstr += "점심: 12:00-13:00\n"
    textstr += "저녁: 18:00-19:30\n"

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

# 장학관 홈페이지 바로가기
@chatbot_narae.route("/homepage",methods=['POST'])
def homepage():
    res = {
        "version": "2.0",
        "template": {
        "outputs": [
                {
                    "basicCard": {
                        #"title": "",
                        "description": "화성시 장학재단 홈페이지입니다.",
                        "thumbnail": {
                            "imageUrl": "https://www.hstree.org/images/hstree/sub/scholarship_img02.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "홈페이지 바로가기",
                                "webLinkUrl": "https://www.hstree.org/"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(res)


# 오픈채팅방 바로가기
@chatbot_narae.route("/openchat",methods=['POST'])
def openchat():
    res = {
        "version": "2.0",
        "template": {
        "outputs": [
                {
                    "basicCard": {
                        #"title": "",
                        "description": "동작나래관의 카카오톡 오픈채팅방 입니다.\n\n비밀번호는 자치회 또는 사무실로 문의해주시길 바랍니다.",
                        "thumbnail": {
                            "imageUrl": "https://www.hstree.org/images/hstree/sub/scholarship_img02.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "오픈채팅 바로가기",
                                "webLinkUrl": "https://open.kakao.com/o/gWZkIcie"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(res)


# 동아리 소개
@chatbot_narae.route("/club",methods=['POST'])
def club():
    res = {
        "version": "2.0",
        "template": {
        "outputs": [              
            {
                "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                            #"title": "",
                            "description": " 화성시 장학관에서 활동하고 있는 동아리들을 소개합니다."
                        },
                        {
                            "title": "동작나래관 자치회",
                            "description": "동작나래관의 다양한 이벤트와 행사들을 계획하고 주관하는 자치회입니다.",
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                            }
                        },
                        {
                            "title": "챗봇 제작 동아리",
                            "description": "화성시 장학관의 다양한 소식과 정보들을 제공하는 챗봇을 제작하고 유지 보수하는 동아리 입니다.",
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                            }
                        },
                        {
                            "title": "보드게임 동아리",
                            "description": "재밌는 보드 게임들을 즐기는 동아리입니다.",
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                            }
                        },
                        {
                            "title": "스포츠 동아리",
                            "description": "배드민턴, 풋살, 볼링 등 다양한 스포츠를 즐기며 활동하는 동아리입니다.",
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                            }
                        },
                        {
                            "title": "영화 감상 동아리",
                            "description": "사생들과 함께 영화관에서 영화를 감상하는 동아리입니다.",
                            "thumbnail": {
                            "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                            }
                        }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(res)

# 장학관 길찾기
@chatbot_narae.route("/road",methods=['POST'])
def road():

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "description": "현재 위치에서 장학관까지 경로입니다.\n카카오맵의 설치가 필요합니다.",
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "장학관 길찾기",
                                "webLinkUrl": "https://map.kakao.com/link/to/화성시장학관동작나래관,37.50000769538511,126.93438539868258e"
                            }
                        ]
                    }
                }
            ]
        }
    }

    return jsonify(res)

# 건의 사항
@chatbot_narae.route("/suggestions",methods=['POST'])
def suggestions():
    res = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "carousel": {
                  "type": "basicCard",
                  "items": [
                    {
                      #"title": "",
                      "description": "챗봇에 대한 건의사항은 아래 버튼을 통한 네이버폼으로 제출 부탁드립니다.",
                      "buttons": [
                                {
                                    "action":  "webLink",
                                    "label": "건의사항 네이버 폼",
                                    "webLinkUrl": "https://naver.me/xUELuo6a"
                                }
                            ]
                      },
                    {
                      #"title": "",
                      "description": "장학관에 대한 건의사항은 아래 버튼을 통한 네이버폼으로 제출 부탁드립니다.",
                      "buttons": [
                                {
                                    "action":  "webLink",
                                    "label": "건의사항 네이버 폼",
                                    "webLinkUrl": "https://naver.me/xUELuo6a"
                                }
                            ]
                      }
                
                  ]
                }
              }
            ]
          }
        }
    return  jsonify(res)


# 화성시장학관 동작나래관 외부인용 챗봇 스킬

# 장학관 소개
@chatbot_narae.route("/introduce",methods=['POST'])
def introduce():

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://raw.githubusercontent.com/Hstree-Dongjak-Narae/ChatBot-Narae/main/%EC%83%81%EC%9A%B1/images/introduce.png",
                        "altText": "장학관 소개"
                    }
                }
            ]
        }
    }

    return jsonify(res)

# 장학관 모집요강
@chatbot_narae.route("/recruitment",methods=['POST'])
def recruitment():

    res = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                  "basicCard": {
                    "description": "2022년 화성시 장학관\n입사생 선발 공고입니다.",
                      "buttons": [
                            {
                                "action":  "webLink",
                                "label": "입사생 선발 공고",
                                "webLinkUrl": "https://www.hstree.org/news/noticeView.do?seq=2020"
                            }
                        ]
                  }
              }
            ]
          }
        }
    return jsonify(res)

# 장학관 위치
@chatbot_narae.route("/position",methods=['POST'])
def position():

    pstr = "화성시장학관 동작나래관은\n"
    pstr += "서울특별시 동작구 성대로 11길 60에 위치해있습니다.\n"
    pstr += "버튼을 클릭하여 네이버 지도에서 위치를 확인할 수 있습니다.\n"

    res = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                 "basicCard":{
                      "description": pstr,
                      "buttons": [
                            {
                                "action":  "webLink",
                                "label": "입사생 선발 공고",
                                "webLinkUrl": "https://naver.me/GlVLep1m"
                            }
                        ]
                  }
              }
            ]
          }
        }
    return jsonify(res)

if __name__ == "__main__":
    #chatbot_narae.run(host='0.0.0.0', port=5001, threaded=True)
    chatbot_narae.run(host='10.128.0.2', port=5001, threaded=True)