import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# set env variable as - export APP_SETTINGS="config.DevelopmentConfig"
app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import models
@app.route('/')
def index():
    return 'Welcome to taxi service!'

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print "Using - " + os.environ['APP_SETTINGS']
    app.run()