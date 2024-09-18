from flask import Flask, jsonify

from handlers.events import *

from db_query.connect import connection

from init_database import command

app = Flask(__name__)

with connection:
    with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
        cursor.execute(command)
        connection.commit()

# app.register_blueprint(auth)
app.register_blueprint(event, url_prefix='/event')
