from decouple import config

from flask import Flask, render_template, request

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def hello():
		return render_template("base.html", title='Home')

	return app






