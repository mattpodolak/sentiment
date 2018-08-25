from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

flapp = Flask(__name__)
flapp.config.from_object(Config)
bootstrap = Bootstrap(flapp)

from app import routes