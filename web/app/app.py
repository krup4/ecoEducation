from flask import Flask, jsonify

from handlers import *

app = Flask(__name__)

#app.register_blueprint(auth)
