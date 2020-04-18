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




@app.route("/")
def index():
   
    return redirect("/register")

@app.route("/register",methods=["POST","GET"])
def info():
    db.create_all()
    if request.method == "POST":
        users_data = schema(request.form["email"], request.form["city"], request.form["username"], request.form["password"])
        user = schema.query.filter_by(email=request.form['email']).first()
        if user is not None:
            var1 = "Error: User is already existing. Please try to register with a new!"
            return render_template("registrationPage.html", Error_message = var1)
    
        db.session.add(users_data)
        db.session.commit()
        
        var2 = 'Registration Success'
       
        return render_template("registrationPage.html", message = var2)
    else:
        return render_template("registrationPage.html")

@app.route('/admin')
def admin():
    user_data = schema.query.all()
    return render_template("admin.html",admin = user_data)
