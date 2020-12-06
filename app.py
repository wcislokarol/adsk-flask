from flask import Flask 
import json 
from flask import render_template


app = Flask(__name__) 

@app.route('/')
def hello_world(): 
	return "Hello hello world!"


@app.route('/api/sample')
def sample_api_hello(): 
	return json.dumps([
		"Kuba", "Michał", "Cezary", "Karol", "Tomek"
	])

@app.route('/index')
def sample_html_page():
	return render_template("hello.html", names=names) 
