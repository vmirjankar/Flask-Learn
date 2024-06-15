from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app=Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(minutes=5) #permanent data in session

@app.route("/")
#home page
def home():
	return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
	#checking for POST method
	if request.method =="POST":
		session.permanent=True
		user = request.form["nm"]
		session["user"]=user
		flash("Login Successful!")
		return redirect(url_for("user"))
	else: #checking for GET method
		if "user" in session:
			flash("Already Logged In!")
			return redirect(url_for("user"))

		return render_template("login.html")

@app.route("/user") 
def user():
	#storing session information
	if "user" in session:
		user = session["user"]
		return render_template("user.html", user=user)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route("/logout")
#logout page
def logout():
	flash("You have been logged out!", "info")
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__=="__main__":
	#run app
	app.run(debug=True)