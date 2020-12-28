from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('usernamemismatch')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Passwordmismatch')
        else:
            session['logged_in'] = True
            flash('loginsuccess')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('logout')
    return redirect(url_for('show_entries'))
