from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! TESTTESTTEST'

@app.route('/test')
def hello_world():
    return 'WOW, TEST!'
