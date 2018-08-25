from app import flapp
from app.forms import InputForm
from flask import render_template, flash, redirect, url_for
from app.indico import single_calc
from app.twitter_search import news_search


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
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    news_search(user)
    return render_template("results.html", labels=labels, values=values)