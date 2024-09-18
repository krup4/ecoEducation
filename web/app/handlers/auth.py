from flask import Flask, Blueprint, request, jsonify
from db_query.auth import *
from handle_jwt import *

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST"])
def login():
    username = request.json.get("login")
    password = request.json.get("password")
    if auth(username, password):
        return jsonify({"jwt": encode_jwt(username)})
    else:
        return jsonify({"error":"incorrect login/password"})

@auth.route('/register', methods = ["POST"])
def register():
    username = request.json.get("login")
    