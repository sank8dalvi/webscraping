from flask import Flask, render_template,request,url_for
from weatherScrape import scrape
import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('weatherPage.html',city="",currentClimate = "")

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	return render_template('weatherPage.html',city=text,currentClimate=scrape(text))

app.run()
