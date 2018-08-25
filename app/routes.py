from app import flapp
from app.forms import InputForm
from flask import render_template, flash
from app.indico import single_calc

@flapp.route('/')
@flapp.route('/index')
def index():
    sent = single_calc(True)
    return render_template('index.html', title='Home', num=sent)

@flapp.route('/about')
def about():
    return render_template('about.html', title='Home')