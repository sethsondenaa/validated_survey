from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = "asdiknooqwerinf345;2rtew8"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
	if len(request.form["name"]) < 1:
		flash("Name cannot be empty!")
		return redirect("/")
	elif len(request.form["comment"]) < 1:
		flash("Comment cannot be empty!")
		return redirect("/")
	elif len(request.form["comment"]) > 120:
		flash("Comment must be shorter than 120 characters!")
		return redirect("/")
	else:	
		return render_template("results.html")

app.run(debug=True)