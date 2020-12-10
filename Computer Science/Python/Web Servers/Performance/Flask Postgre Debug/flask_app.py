from flask import Flask
app = Flask(__name__) # WSGI app

@app.route('/')
def hello_world():
    return 'Hello, World!'