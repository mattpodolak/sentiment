from app import flapp
from app.forms import InputForm
from flask import render_template, flash
from app.twitter_search import twittersearch

@flapp.route('/')
@flapp.route('/index')
def index():
    return render_template('index.html', title='Home')

@flapp.route('/about')
def about():
    return render_template('about.html', title='Home')