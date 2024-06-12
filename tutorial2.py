from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/<name>")
#home page
def home(name):
	#add /<name> to the url to run 
	return render_template("index.html", content=["tim", "joe", "bill"])

if __name__=="__main__":
	#run app
	app.run()