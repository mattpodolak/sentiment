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
        user = form.twitter.data
        flash('Input ' + user)
        return redirect(url_for('results', user=user))
    return render_template('calculate.html', title='Calculate', form=form)

@flapp.route('/about')
def about():
    return render_template('about.html', title='About')

@flapp.route('/results/<user>')
def results(user):
    # insert twitter scrap here
    # insert indico calls here
    # insert graph here
    labels = ["Jan 20","Jan 21","Jan 22","Jan 23","Jan 24","Jan 25","Jan 26","Jan 27"]
    values = batch_calc(["i hate mcdons", "i love mcdons", "mcdons is alright", "idk what mcdons is", "i hate mcdons", "i love mcdons", "mcdons is alright", "idk what mcdons is"])
    return render_template("results.html", labels=labels, values=values)