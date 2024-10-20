from app import app
from flask import render_template

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title='GOAT')

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.addForm()
    if form.validate_on_submit():
        print("submitted title: ", form.title.data)
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', current_title='About', form=form)