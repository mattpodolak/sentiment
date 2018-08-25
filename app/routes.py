from app import flapp
from app.forms import InputForm
from flask import render_template, flash
from app.indico import single_calc

@flapp.route('/')
@flapp.route('/index')
def index():
    return render_template('index.html', title='Home')

@flapp.route('/calculate', methods=['GET', 'POST'])
def calculate():
    form = InputForm()
    if form.validate_on_submit():
        user = form.twitter.data
        flash('Twitter input ' + user)
        return redirect(url_for('results', sentiment=user))
    return render_template('calculate.html', title='Calculate Sentiment', form=form)

@flapp.route('/about')
def about():
    return render_template('about.html', title='About')

@flapp.route('/results/<sentiment>')
def results(sentiment):
    return render_template('results.html', title='Results', sentiment=sentiment)