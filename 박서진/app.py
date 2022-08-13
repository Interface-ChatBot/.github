from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask'

@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    app.run() 