# This line of code is importing various modules and objects from different files and packages.
from flask import render_template, request, redirect, url_for, flash
from app import app, db, cipher_suite
from app.models import Password

# `@app.route('/')` is a decorator in Flask that associates the following function with the specified
# URL route. In this case, it associates the `index()` function with the root URL ("/"). So when a
# user visits the root URL of the application, the `index()` function will be executed.
@app.route('/')
def index():
# The code `passwords = Password.query.all()` retrieves all the passwords from the database by
# querying the `Password` model.
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/add_password', methods=['GET', 'POST'])
def add_password():

# This code block is handling the addition of a new password to the database.
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        # The line `encrypted_password = cipher_suite.encrypt(password.encode()).decode()` is encrypting the
        # password using a cipher suite.
        encrypted_password = cipher_suite.encrypt(password.encode()).decode()

        # The code is creating a new instance of the `Password` model with the provided `name`, `username`,
        # and `encrypted_password` values.
        new_password = Password(name=name, username=username, encrypted_password=encrypted_password)
        db.session.add(new_password)
        db.session.commit()

        # This code is handling the addition of a new password to the database.
        flash('Password added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_password.html')


@app.route('/view_password/<int:id>')
def view_password(id):
    # This code block is defining a route `/view_password/<int:id>` that handles a GET request. It
    # retrieves a password from the database based on the provided `id` parameter. If a password is found,
    # it decrypts the encrypted password using the `cipher_suite` and renders the `view_password.html`
    # template with the password and decrypted password as variables.
    password = Password.query.get(id)
    if password:
        decrypted_password = cipher_suite.decrypt(password.encrypted_password.encode()).decode()
        return render_template('view_password.html', password=password, decrypted_password=decrypted_password)
    else:
        flash('Password not found', 'danger')
        return redirect(url_for('index'))


@app.route('/edit_password/<int:id>', methods=['GET', 'POST'])
def edit_password(id):
# The code `password = Password.query.get(id)` is retrieving a password from the database based on the
# provided `id` parameter.
    password = Password.query.get(id)
    if password:
        # This code block is handling the editing of a password in the database.
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            new_password = request.form['password']
            encrypted_password = cipher_suite.encrypt(new_password.encode()).decode()
            password.name = name
            password.username = username
            password.encrypted_password = encrypted_password

            db.session.commit()
            flash('Password edited successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('edit_password.html', password=password)
    else:
        flash('Password not found', 'danger')
        return redirect(url_for('index'))

@app.route('/edit_password_name/<int:id>', methods=['GET', 'POST'])
def edit_password_name(id):
    # This code block is handling the editing of the name of a password in the database.
    password = Password.query.get(id)
    if password:
        if request.method == 'POST':
            name = request.form['name']
            password.name = name
            db.session.commit()
            flash('Password name edited successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('edit_password_name.html', password=password)
    else:
        flash('Password not found', 'danger')
        return redirect(url_for('index'))

@app.route('/edit_password_username/<int:id>', methods=['GET', 'POST'])
def edit_password_username(id):
    # This code block is handling the editing of the username of a password in the database.
    password = Password.query.get(id)
    if password:
        if request.method == 'POST':
            username = request.form['username']
            password.username = username
            db.session.commit()
            flash('Username edited successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('edit_password_username.html', password=password)
    else:
        flash('Password not found', 'danger')
        return redirect(url_for('index'))    

@app.route('/delete_password/<int:id>', methods=['POST'])
def delete_password(id):
    # This code block is handling the deletion of a password from the database.
    password = Password.query.get(id)
    if password:
        if request.form['confirm'] == 'yes':
            db.session.delete(password)
            db.session.commit()
            flash('Password deleted successfully!', 'success')
        else:
            flash('Password has not been deleted', 'danger')
    else:
        flash('Password not found', 'danger')
    return redirect(url_for('index'))
