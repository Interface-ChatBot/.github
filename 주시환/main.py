# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!"


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


@application.route("/event", methods=['POST'])
def event():
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "description": "인터페이스의 행사들을 소개합니다!"
                            },
                            {
                                "title": "인터페이스 프로그래밍 전시회",
                                "description": "인터페이스에서 자체적으로 진행하는 프로그래밍 전시회입니다.",
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/Eyjyd/btrQw2OoFRH/KXZMjlfXx0ZGAM0c2msxO0/800x800.jpg"
                                }

                            },
                            {
                                "title": "인터페이스 인커톤 행사",
                                "description": "인터페이스와 해커톤을 합한 말로, 인터페이스의 큰 행사 중 하나입니다.",
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/ka43N/btrQDvBvB7N/jbZxXDQy91rBKIKPSRXTmK/800x800.jpg"
                                }
                            },
                            {
                                "title": "인터페이스 스터디",
                                "description": "파이썬, c언어, 알고리즘등 많은 스터디들이 준비되어 있습니다.",
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/nuAWB/btrQz6CKK27/QWPgYKRec4qmmvh0wbwIjk/800x800.jpg"
                                }
                            }
                        ]
                    }

                }

            ]
        }
    }

    return jsonify(res)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
