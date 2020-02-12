from flask import url_for, render_template, redirect
from flask import current_app as app
from forms import ContactForm, SignupForm, TemperatureSubmissionForm


@app.route('/')
def home():
    return render_template('index.html',
                           template='home-template')

@app.route('/temperature', methods=['GET','POST'])
def temperature():
    form = TemperatureSubmissionForm()
    first = True
    if form.validate_on_submit():
        print("form.validate_on_submit():", True)
        return redirect(url_for('success'), code=200)
        #return redirect('/success')
    else:
        print("form.validate_on_submit():", False)
        if not first:
            return redirect(url_for('success'), code=200)
    first = False
    return render_template('temperature.html',
                           form=form,
                           template='form-template')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'), code=200)
    return render_template('contact.html',
                           form=form,
                           template='form-template')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('success'), code=200)
    return render_template('signup.html',
                           form=form,
                           template='form-template')


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html',
                           template='success-template')