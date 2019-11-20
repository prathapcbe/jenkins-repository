from flask import Flask,url_for,jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'manickam!'

@app.route('/foo', methods=['POST']) 
def foo():
    data = request.json
    print(data.get('a')+data.get('b'))
    return jsonify(data)

@app.route('/sum/<int:a_value>',methods = ['POST'])
def addtion(a_value):
    add=a_value+5
    return "%d" % add

@app.route('/sub/<int:s_value>')
def subtraction(s_value):
    sub=s_value-5
    return "%d" % sub

@app.route('/mul/<int:m_value>')
def multiply(m_value):
    mul=m_value*5
    return "%d" % mul

@app.route('/div/<int:d_value>')
def division(d_value):
    div=d_value/5
    return "%f" % div
   
    
    
  
@app.route('/name')
def hello_world1():
    return 'prathap!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#methods=['POST''GET']
#<int:value>',methods=['POST''GET']