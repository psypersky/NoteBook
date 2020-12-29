import logging
from errors import APIError

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

from flask import Flask, jsonify
from db import get_users
from lib import encrypt_users
from time import sleep

app = Flask(__name__)  # WSGI app

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/users')
def hello_world():
    logging.info('getting users')
    users = get_users()
    print(users[0]['first_name'])
    encrypted_users = encrypt_users(users, 1000)
    sleep(10)
    print(encrypted_users)
    return jsonify(encrypted_users)