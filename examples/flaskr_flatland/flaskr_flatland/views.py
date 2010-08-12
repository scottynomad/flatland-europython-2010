from flaskr_flatland import app, forms
from flaskr_flatland.forms import (
    RegistrationForm,
    PasswordCompareElement,
    PasswordCompareForm
)
from flaskr_flatland.util import error_filter
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

from flatland.out.markup import Generator
from functools import partial
from jinja2 import Markup

Generator = partial(Generator, markup_wrapper=Markup,
                               auto_filter=True,
                               filters=[error_filter])

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm.from_flat(request.form)
    if request.method == 'POST' and form.validate():
        # Create the user object
        flash('Thanks for registering: %s' % form['username'].u)
        return redirect(url_for('login'))
    gen = Generator()
    return render_template('register.html', form=form, generator=gen)

@app.route('/passwords-form', methods=['GET', 'POST'])
def passwords1():
    form = forms.PasswordCompareForm.from_flat(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks!')
    gen = Generator()
    return render_template('password.html', form=form, generator=gen)

@app.route('/passwords-element', methods=['GET', 'POST'])
def passwords2():
    form = forms.PasswordCompareElement.from_flat(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks!')
    gen = Generator()
    return render_template('password.html', form=form, generator=gen)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = forms.ContactForm.from_flat(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks!')
    else:
        form.set_default()
    gen = Generator()
    return render_template('contact.html', form=form, generator=gen)

