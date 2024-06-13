from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/")
#home page
def home():
	return render_template("index.html", content="Testing")

if __name__=="__main__":
	#run app
	app.run(debug=True)