from flask import Flask, Blueprint, request, jsonify

from psycopg2 import extras

from db_query.connect import connection
from db_query.organizer_queries import *
from handle_jwt import *

from uuid import uuid4

organizer = Blueprint("organizer", __name__, url_prefix="/org")


@organizer.route("/register", methods=['POST'])
def add():
    data = request.json
    if ('proof' not in data.keys()):
        return jsonify({"reason": "no proofs"}), 400
    if (data.get('proof') == ''):
        return jsonify({"reason": "no proofs"}), 400
    query = reg_org(uuid.uuid4(), data)
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()
            return jsonify({"status": "ok"}), 200


@organizer.route("/login", methods=["POST"])
def login():
    loginS = request.json.get("login")
    password = request.json.get("password")
    # return jsonify({"asdf": auth_check(username, password)})
    # return jsonify(login_check(loginS, password)), 200

    if login_check(loginS, password):
        return jsonify({"login": "ok"}), 200
    else:
        return jsonify({"error": "incorrect login/password"}), 400


@organizer.route("/show", methods=['GET'])
def show():
    query = "SELECT * FROM organizers"
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return jsonify(data), 200
