from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import urllib3

app = Flask(__name__)

#with open('/etc/config.json') as config_file:
 # config = json.load(config_file)

#app.config['SECRET_KEY'] = config.get('SECRET_KEY')

from storms-burrow import routes
