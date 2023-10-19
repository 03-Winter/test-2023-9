from flask import Flask,render_template
from random import randint
app=Flask(__name__)

hero=['赵萨满','钱多年','孙五年','李四篇','周威威','武物外','郑成功','王北斗']


@app.route('/index')
def index():
    return render_template('index.html',heros=hero)


@app.route('/choujiang')
def choujiang():
    num=randint(0,len(hero)-1)
    return render_template('index.html',heros=hero,h=hero[num])

app.run(debug=True)
