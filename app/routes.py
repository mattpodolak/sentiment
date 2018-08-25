from app import flapp
from app.forms import InputForm
from flask import render_template, flash, redirect, url_for
from app.indico import single_calc, batch_calc, avg_batch_calc
from app.search import news_search
from datetime import datetime, timedelta

@flapp.route('/')
@flapp.route('/index')
def index():
    return render_template('index.html', title='Home')

@flapp.route('/calculate', methods=['GET', 'POST'])
def calculate():
    form = InputForm()
    if form.validate_on_submit():
        search_input = form.search_input.data
        flash('Sentiment analysis for ' + search_input)
        return redirect(url_for('results', search_input=search_input))
    return render_template('calculate.html', title='Calculate', form=form)

@flapp.route('/about')
def about():
    return render_template('about.html', title='About')

@flapp.route('/results/<search_input>')
def results(search_input):
    days_to_subtract = 30
    today = datetime.today()
    all_scans = []
    labels = []
    values = []
    for i in range(0, 31):
        date = today - timedelta(days=days_to_subtract-i)
        date_str = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        labels.append(date_str)
        scan = news_search(search_input, date_str)
        all_scans.append(scan)
        if scan:
            values.append(avg_batch_calc(scan))
        else:
            values.append(0)           
    
    return render_template("results.html", labels=labels, values=values, scan=all_scans)