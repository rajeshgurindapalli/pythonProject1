from flask import *
import sqlite3


#create the object of Flask
from pymongo import MongoClient

app  = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.FLASK
user = db.user

#creating our routes
@app.route('/')
def Index():
    name = 'KL University - CSE [Honors] - Y21 - PFSD - S17'
    return render_template('index.html', data = name)

@app.route('/contact')
def Contact():
    return render_template('contact.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route("/login")
def my_index_page():
    return render_template("login.html")

@app.route("/newuser")
def my_newuser_register_page():
    return render_template("register.html")

@app.route("/registeruser", methods=['POST','GET'])
def my_regiser_user():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    entered_password = entered_password.lower()
    entered_email = request.form.get("email")
    entered_mobileno = request.form.get("mobileno")

    print(entered_username, entered_password, entered_email, entered_mobileno)

    user.insert_one({'username':entered_username,'password':entered_password,'email':entered_email,'mobileno':entered_mobileno})

    return "User Registered Successfully"


@app.route("/loginuser", methods=['POST','GET'])
def my_login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")


#run flask app
if __name__ == "__main__":
    app.run(debug=True)






