from flask import Flask
import requests
 
app = Flask(__name__)


@app.route('/rss')
def index1():
    req = requests.get(f'http://127.0.0.1:1200')
    return req.text

@app.route('/rss/<path:name>')
def index(name):

    req = requests.get(f'http://127.0.0.1:1200/{name}')
    return req.text

 
@app.route('/test')
def test():
    return "Hello test."
 
@app.route('/user/<username>')
def show_user(username):
    return 'User: %s' % username
 
if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
 
