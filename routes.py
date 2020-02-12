from flask import url_for, render_template, redirect, flash
from flask import current_app as app
from forms import ContactForm, SignupForm, TemperatureSubmissionForm


@app.route('/')
def home():
    return render_template('index.html',
                           template='home-template')

@app.route('/temperature', methods=['GET','POST'])
def temperature():
    form = TemperatureSubmissionForm()


    print(form.errors)
    if request.method == 'POST':
        emp_id=request.form['emp_id']
        emp_name=request.form['emp_id']
        temperature=request.form['temperature']
        print(f'{emp_id}, {emp_name}, {temperature}')

    if form.validate():
    # Save the comment here.
        flash('Thanks for submission ' + emp_id)
    else:
        flash('Error: All the form fields are required. ')

    if form.validate_on_submit():
        print("form.validate_on_submit():", True)
        return redirect(url_for('success'), code=200)
    else:
        print("form.validate_on_submit():", False)

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