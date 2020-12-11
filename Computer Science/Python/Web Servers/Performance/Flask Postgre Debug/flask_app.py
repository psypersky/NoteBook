from flask import Flask
from db import get_users
from lib import encrypt_users
app = Flask(__name__) # WSGI app

@app.route('/')
def hello_world():
    users = get_users()
    print(users)
    encrypted_users = encrypt_users(users)
    print(encrypted_users)
    return str(encrypted_users)