# flask_blog/views.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('UserNamemismatch')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Passwordmismatch')
        else:
            session['logged_in'] = True
            flash('login success')
            return redirect('/')
    return render_template('login.html')
 

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('logout')
    return redirect(url_for('show_entries')) # return redirect('/') 
