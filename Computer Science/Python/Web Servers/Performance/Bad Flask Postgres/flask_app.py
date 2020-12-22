from flask import Flask
from db import get_users, DataReader
from lib import encrypt_users
from time import sleep

app = Flask(__name__)  # WSGI app


@app.route('/')
def hello_world():
    users = get_users()
    print(users)
    encrypted_users = encrypt_users(users)
    print(encrypted_users)
    return str(encrypted_users)


@app.route('/v2')
def route_v2():
    data_reader = DataReader()
    sleep(2)  # Fake network latency
    users = data_reader.get_users()
    encrypted_users = encrypt_users(users, times=1000) # CPU ussage
    print(encrypted_users)
    return str(encrypted_users)