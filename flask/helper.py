# create a hello world flask app
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

def hello_world():
    pagetitle = 'Home Page'
    header = 'Welcome to the Home Page'
    items = ['French', 'Spanish', 'German', 'Chinese']
    return render_template('index.html', pagetitle=pagetitle, header=header, items=items)

def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template('name.html')
    


def get_help():
    return render_template('help.html')



