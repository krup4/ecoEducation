from flask import Flask, Blueprint, request

from psycopg2 import extras

from db_query.connect import connection
from db_query.events_queries import insert_event, delete_event

event = Blueprint("event", __name__)


@event.route("/add", methods=['POST'])
def add():
    data = request.json
    query = insert_event(data.get('time'), data.get('latitude'), data.get('longitude'), data.get(
        'name'), data.get('cost'), data.get('tags'), data.get('description'))
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()


@event.route('/delete', methods=['POST'])
def delete():
    uid = request.json.get('id')
    query = delete_event(uid)
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()
