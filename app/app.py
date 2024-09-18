from flask import Flask, jsonify
import os
import psycopg2
from psycopg2 import extras
import bcrypt

from init_database import command

app = Flask(__name__)

salt = bcrypt.gensalt()

user = os.environ['POSTGRES_USERNAME']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
database = os.environ['POSTGRES_DATABASE']
connection = psycopg2.connect(user=user,
                              password=password,
                              host=host,
                              port=port,
                              database=database)


with connection:
    with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
        cursor.execute(command)
        connection.commit()


@app.route('/api/ping', methods=['GET'])
def send():
    return jsonify({"status": "ok"}), 200


@app.route('/api/users', methods=['GET'])
def users():
    query = "SELECT * FROM users"
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return jsonify(data), 200
