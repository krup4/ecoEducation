from flask import Flask, Blueprint, request, jsonify
from db_query.auth import *
from handle_jwt import *

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if auth(username, password):
        return jsonify({"jwt": encode_jwt(username)})
    else:
        return jsonify({"error":"incorrect login/password"})

@auth.route('/register', methods = ["POST"])
def register_user():
    username = request.json.get("username")
    password = request.json.get("password")
    full_name = request.json.get("full_name")
    try:
        register(username, password, full_name, 0)
        return jsonify({"result":"OK"})
    except:
        return jsonify({"result":"SOMETHING WORK"})