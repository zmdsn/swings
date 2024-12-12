from flask import Flask
import requests
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    # 这里可以使用requests.request来实现各种http方法
    req = requests.get('http://127.0.0.1:400')
    # 响应体返回，这里是字符串
    return req.text
 
 
@app.route('/proxy')
def proxy():
    return "Hello Flask."
 
 
if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
 