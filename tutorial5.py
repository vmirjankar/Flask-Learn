from flask import Flask, redirect, url_for, render_template, request, session
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
		return redirect(url_for("user"))
	else: #checking for GET method
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("login.html")

@app.route("/user") 
def user():
	#storing session information
	if "user" in session:
		user = session["user"]
		return f"<h1>{user}</h1>"
	else:
		return redirect(url_for("login"))

@app.route("/logout")
#logout page
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__=="__main__":
	#run app
	app.run(debug=True)