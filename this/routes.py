from app import app
from flask import render_template, send_from_directory

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title='Home')

@app.route('/sitemap.html')
def sitemap():
    return render_template('sitemap.html', current_title='Sitemap')

@app.route('/sitemap.xml')
def sitemap_template():
    return send_from_directory('.', 'sitemap.xml')

@app.route('/about')
def about():
    return render_template('about.html', current_title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', current_title='Contact')