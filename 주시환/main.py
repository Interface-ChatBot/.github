from flask import Flask, request, jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!"

#인터페이스 집부 구성원 안내
@application.route("/executive_member", methods=['POST'])
def executive_member():
    req = request.get_json()
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "회장:아무개 wntlghks0107@naver.com\n부회장:이무개 wntis0107@naver.com\n총무:길동 wlso@naver.com"
                    }
                }
            ]
        }
    }
    return jsonify(res)

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
    application.run(host='0.0.0.0', port=5000, threaded=True)
