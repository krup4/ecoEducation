from flask import Flask, jsonify

from handlers.events import event
from handler.auth import auth

from db_query.connect import connection
from psycopg2 import extras
from init_database import command

app = Flask(__name__)

with connection:
    with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
        cursor.execute(command)
        connection.commit()

# app.register_blueprint(auth)
app.register_blueprint(event)
app.register_blueprint(auth)

@app.route('/ping', methods=['GET'])
def send():
    return jsonify({"status": "ok"}), 200
