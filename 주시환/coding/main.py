from flask import Flask

print('[Hello Flask!]')
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hi Flask!'

if __name__=='__main__':
    app.run(debug=True)
