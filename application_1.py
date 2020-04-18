import os
from schema import *
from flask import Flask, session, render_template,request,redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
# db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    # return render_template("registrationPage.html")
    return redirect("/register")

@app.route("/register",methods=["POST","GET"])
def info():
    db.create_all()
    if request.method == "POST":
        users_data = schema(request.form["email"], request.form["city"], request.form["username"], request.form["password"])
        # email=request.form.get("email") 
        # city=request.form.get("city") 
        # username=request.form.get("username") 
        # password=request.form.get("password")
        db.session.add(users_data)
        db.session.commit()
        # return render_template("Details.html",email=email,city=city,username=username, password = password)
        return render_template("registrationPage.html")
    else:
        return render_template("registrationPage.html")
