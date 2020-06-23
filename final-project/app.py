from functions import concat, grouped, by_region, plot_new, plot_total, maxday, apology
from flask import Flask, flash, redirect, render_template, request, session, url_for
import pandas as pd
from flask_session import Session
from tempfile import mkdtemp
from datetime import date




app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/results")
def tables():

	today = str(date.today())
	region = request.args.get("region")
	dates = request.args.get("dates")

	if dates > today:
		return apology("You Must to Provide Date Before Tomorrow",400)

	elif not dates:
		return apology("You Must to Provide a Date",400)

	else: 
		dates = dates.split("-")
		month = int(dates[1])
		day = int(dates[2])
		data = by_region(grouped(concat(int(dates[1]),int(dates[2]))),region)
		data.to_csv("data.csv")
		return render_template('results.html',dates=dates, region=region, tables=[data.to_html(classes='data').replace('border="1"','border="0"')], titles=data.columns.values)


@app.route("/plots")
def plotting():

	data = pd.read_csv("data.csv")
	graph_total=plot_total(data)
	graph_new=plot_new(data)
	
	return render_template('plots.html',graph_total=graph_total, graph_new=graph_new)
	
