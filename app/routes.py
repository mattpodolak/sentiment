from app import flapp
from app.forms import InputForm
from flask import render_template, flash, redirect, url_for
from app.indico import single_calc, batch_calc
from app.search import news_search


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
    # insert news scrape here
    scan = news_search(search_input)
    # insert indico calls here
    #labels = ["Jan 20","Jan 21","Jan 22","Jan 23","Jan 24","Jan 25","Jan 26","Jan 27"]
    labels = [x for x in range(0, 31)]
    values = batch_calc(scan)
    return render_template("results.html", labels=labels, values=values, scan=scan)