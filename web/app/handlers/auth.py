from flask import Blueprint, request, jsonify
from db_query.auth import *
from handle_jwt import *

auth = Blueprint("auth", __name__, url_prefix='/auth')


@auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    # return jsonify({"asdf":auth_check(username, password)})
    if auth_check(username, password):
        return jsonify({"jwt": encode_jwt(username)}), 200
    else:
        return jsonify({"error": "incorrect login/password"}), 400


@auth.route('/register', methods=["POST"])
def register_user():
    username = request.json.get("username")
    password = request.json.get("password")
    full_name = request.json.get("full_name")
<<<<<<< HEAD
    
    #return jsonify({"asf": register(username, password, full_name, 0)})
    return jsonify({"jwt": encode_jwt(username)}), 200
    
=======
    try:
        return jsonify({"asf": register(username, password, full_name, 0)}), 200
        # return jsonify({"result": "OK"}), 200
    except:
        return jsonify({"result": "SOMETHING WORKS WRONG"}), 400
>>>>>>> 1db16d7e47d5eb15cc2c03b1a2088806dd2d710f
