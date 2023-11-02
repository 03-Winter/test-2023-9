from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    uname=request.args.get('uname')
    pwd=request.args.get('pwd')

    if uname=='你好':
        return f'hello!{uname}'
    else:print('error')

app.run(debug=True)