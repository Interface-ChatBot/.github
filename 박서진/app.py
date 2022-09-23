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
                    "simpleText": {
                        "text": "�������б� �߾ӵ��Ƹ� �������̽� ����"
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
    
    res = {
         "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "������Ʈ ����ȸ"
                    }
                }
            ]
        }
    }
    return jsonify(res)


# Information on the number of people Interface members
@application.route("/people",methods = ['POST'])
def people():
    req = request.get_json()
    
    generation_type = req["action"]["detailParams"]["generation_type"]["value"]
    
    people = 0
    
    if generation_type == "30��":
        people = 10
    elif generation_type == "31��":
        people = 20
    elif generation_type == "32��":
        people = 34
    elif generation_type == "33��":
        people = 45
    elif generation_type == "34��":
        people = 50
    elif generation_type == "35��":
        people = 70
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "[����� �ο� ��]\n" + generation_type + " : " +str(people) + "��"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
