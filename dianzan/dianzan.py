from flask import Flask,render_template,request

app=Flask(__name__)
data=[
    {'id':0,'name':'jack','num':0},
    {'id':1,'name':'jane','num':0},
    {'id':2,'name':'jia','num':0}
]
@app.route('/dianzan')
def dianzan():
    id=request.args.get('id')
    print(f'给{id}点赞')
    data[int(id)]['num'] +=1
    return render_template('dianzan.html',data=data)

app.run(debug=True)