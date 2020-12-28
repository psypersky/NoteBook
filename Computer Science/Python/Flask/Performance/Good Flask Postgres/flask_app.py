import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

from flask import Flask
from db import get_users
from lib import encrypt_users
from time import sleep

app = Flask(__name__)  # WSGI app


@app.route('/users')
def hello_world():
    logging.info('getting users')
    users = get_users()
    print(users)
    encrypted_users = encrypt_users(users)
    print(encrypted_users)
    return str(encrypted_users)