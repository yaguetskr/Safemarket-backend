from back import app,products
from flask import render_template



@app.route('/')
@app.route('/home')
def home_page():

     return 'Hello world!'
