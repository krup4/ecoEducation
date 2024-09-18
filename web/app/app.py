from flask import Flask, jsonify

from handlers.events import *

app = Flask(__name__)

# app.register_blueprint(auth)
app.register_blueprint(event, url_prefix='/event')
