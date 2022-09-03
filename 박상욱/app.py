from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#url
@app.route('/',methods=['GET')
def index():
    return 'Hello Flask'

#url
@app.route('/',methods=['POST')
def index():
    content = request.get_json()
    content = content['userRequest']['utterance']

    content = content.replace("\n","")
    print(content)

    if content = u"������ �޴�"
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "�׽�Ʈ�Դϴ�."
                        }
                    }
                ]
            }
        }
    else:
        
    return 'Hello Flask'

# membership fee
@app.route('/fee')
def fee():
    if method == "POST":
        # payloads = request.get_json()
        # pprint.pprint(payloads)
        _ret = {"version": "2.0",
                "template": {"outputs": [{"simpleText": {"text": "hello"}}]
                                }
                }

    return jsonify(_ret), 200

    
    # return { "freshman": "15000","nofreshman": "10000"}

# Club Wi-Fi password
@app.route('/wifi')
def wifi():
    return {
        "interface518": "518interface",
        "interface518 5G": "518interface"
    }

@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    app.run()