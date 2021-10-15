import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    services = list(mongo.db.services.find())
    return render_template("services.html", services=services)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_services", methods=["GET", "POST"])
def add_services():
    if request.method == "POST":
        service = {
            "url_img": request.form.get("url_img"),
            "category_name": request.form.get("category_name"),
            "your_name": request.form.get("your_name"),
            "job_description": request.form.get("job_description"),
            "contact_us": request.form.get("contact_us"),
            "email_us": request.form.get("email_us"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.services.insert_one(service)
        flash("Task Successfully Added")
        return redirect(url_for("home"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_services.html", categories=categories)


@app.route("/edit_service/<service_id>", methods=["GET", "POST"])
def edit_service(service_id):
    if request.method == "POST":
        submit = {
            "url_img": request.form.get("url_img"),
            "category_name": request.form.get("category_name"),
            "your_name": request.form.get("your_name"),
            "job_description": request.form.get("job_description"),
            "contact_us": request.form.get("contact_us"),
            "email_us": request.form.get("email_us"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.services.update({"_id": ObjectId(service_id)}, submit)
        flash("Task Successfully Updated")
       
    service = mongo.db.services.find_one({"_id": ObjectId(service_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_service.html", service=service, categories=categories)


@app.route("/delet_service/<service_id>")
def delet_service(service_id):
     mongo.db.services.remove({"_id": ObjectId(service_id)})
     flash("Task Successfully Deleted")
     return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)