from flask import Flask
from db import get_users
app = Flask(__name__) # WSGI app

@app.route('/')
def hello_world():
    users = get_users()
    print(users)
    return str(users)