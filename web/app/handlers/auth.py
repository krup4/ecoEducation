from flask import Flask, Blueprint, request
from db_query.auth import *

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        username = request.json.get("login")
        password = request.json.get("password")
        if (auth(username, password)):
            return 

