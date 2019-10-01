from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/homepage")
def index():
    return render_template('index.html')

@app.route("/homepage", methods=['POST', 'GET'])
def validation():
    valid_username = request.form['username']
    valid_password = request.form['password']
    valid_verify = request.form['verify']
    valid_email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if int(len(valid_username)) <= 0:
        username_error = 'Thats not a valid username'
        valid_username = ''
    else:
        if int(len(valid_username)) < 3 or int(len(valid_username)) > 20:
            username_error = 'Thats not a valid username'
            valid_username = ''
    
    if int(len(valid_password)) <= 0:
        password_error = 'Thats not a valid password'
        valid_password = ''
    else:
        if int(len(valid_password)) < 3 or int(len(valid_password)) > 20:
            password_error = 'Thats not a valid password'
            valid_password = ''

    if int(len(valid_verify)) <= 0:
        verify_error = 'Password do not match'
        valid_verify = ''
    else:
        if valid_password != valid_verify:
            verify_error = 'Password do not match'
            valid_verify = ''  
    
    if int(len(valid_email)) > 0:
        if "@" not in valid_email and "." not in valid_email and " " not in valid_email:
            email_error = 'Thats not a valid email'
            email = ''
        elif int(len(valid_email)) < 3 or int(len(valid_password)) > 20:
            email_error = 'Thats not a valid email'
            email = ''

    if not username_error and not password_error and not verify_error and not email_error:
        valid_username = str(valid_username)
        return redirect('/welcome_page?username={0}'.format(valid_username))
    else:
        return render_template('homepage.html', username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error, valid_username=valid_username, valid_password=valid_password, valid_verify=valid_verify, valid_email=valid_email)

@app.route("/welcome_page")
def welcome():
    valid_username = request.args.get('username')
    return render_template('welcome_page.html', valid_username = valid_username)

app.run()