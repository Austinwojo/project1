import os
import requests
import json
import helpers import *

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/",methods=["GET","POST"])
@login_required
def index():
    return "Project 1: TODO"

@app.login("/login",methods=["get","post"])
def login():
    log_in_message = ""
    if request.method=="POST"
        email=request.form.get('email')
        userPassword=request.form.get('userPassword')
        emailLogIn=request.form.get('emailLogIn')
        userPasswordLogIn=request.form.get('userPasswordLogIn')
        if emailLogIN==None:
            data=db.execute("SELECT username FROM users").fetchall()
            for i in range(len(data)):
                if data[i]["username"]==email:
                    log_in_message="Username already exists. Please enter a new user name"
                    return render_template('login.html', log_in_message=log_in_message)
            db.execute("INSERT INTO users (username,password) VALUES (:a,:b)",{"a":email,"b":userPassword})
            db.commit()
            log_in_message="Success!"
        else:
            data=db.execute("SELECT * FROM users WHERE username = :a",{"a":emailLogIN}).fetchone()
            if data!=None:
                if data.username==emailLogIN and data.password==userPasswordLogIn:
                    session["username"]=emailLogIN
                    return redirect(url_for("index"))
                else:
                    log_in_message="You have entered the wrong email or password."
            else:
                log_in_message="You have entered the wrong email or password."
    return render_template('login.html', log_in_message=log_in_message)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
