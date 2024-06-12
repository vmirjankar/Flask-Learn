from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route("/")
#home page
def home():
	return "Hello! This is the main page <h1>HELLO<h1>"

@app.route("/<name>") #passes the text as parameter to the user func
def user(name):
	return f"Hello {name}!"

@app.route("/admin/")
def admin():
	return redirect(url_for("user", name="Admin!")) #redirects to the specified function

if __name__=="__main__":
	#run app
	app.run()
