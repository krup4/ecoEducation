from flask import Flask, Blueprint, request, jsonify

from psycopg2 import extras

from db_query.connect import connection
from db_query.events_queries import *

from uuid import uuid4

event = Blueprint("event", __name__, url_prefix="/event")


@event.route("/add", methods=['POST'])
def add():
    data = request.json
    query = insert_event(uuid4(), data.get('time'), data.get('adress'), data.get(
        'name'), data.get('cost'), data.get('tags'), data.get('description'))
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()
            return jsonify({"status": "ok"}), 200


@event.route('/delete', methods=['POST'])
def delete():
    uuid = request.json.get('uuid')
    query = delete_event(uuid)
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()
            return jsonify({"status": "ok"}), 200


@event.route('/edit', methods=['POST'])
def edit():
    uuid = request.json.get('uuid')
    data = request.json
    # print(data, uuid)
    # return jsonify(data), 200
    query = edit_event(uuid, data)
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()
            return jsonify({"status": "ok"}), 200


@event.route("/show", methods=['GET'])
def show():
    query = "SELECT * FROM events"
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return jsonify(data), 200
