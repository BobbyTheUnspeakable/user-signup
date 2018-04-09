from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def validate(string):
    if len(string) < 3 or len(string) > 20:
        return False
    else:
        return True

@app.route("/", methods=["POST", "GET"])
def index():
    
    return render_template('sign-in.html') 

@app.route("/welcome.html", methods=['POST', "GET"])
def welcome():
    username = str(request.form.get('username'))
    password = str(request.form.get('pword'))
    verified_password = str(request.form.get('verpword'))
    email = str(request.form.get('email'))
    list_email = list(email)

    if validate(username) == False:
        user_error = "Usernames should be between 3 and 20 characters"
        return redirect("/?error=" + user_error)
    if username.isalnum() == False:
        user_error = "Username cannot contain spaces."
        return redirect("/?error=" + user_error)

    if validate(password) == False:
        pw_error = "Passwords should be between 3 and 20 characters"
        return redirect("/?error=" + pw_error)
    if password.isalnum() == False:
        pw_error = "Password cannot contain spaces."
        return redirect("/?error=" + pw_error)

    if verified_password != password:
        vpw_error = "Passwords do not match"
        return redirect("/?error=" + vpw_error)

    if email != '':
        if validate(email) == False:
            email_error = "emails should be between 3 and 20 characters"
            return redirect('/?error=' + email_error)
        if ('@' not in list_email) == True and ('.' not in list_email) == True:
            email_error = "Not a valid email"
            return redirect('/?error=' + email_error)

    return render_template('welcome.html', username = username)
    #user_error=user_error, pw_error=pw_error, vpw_error=vpw_error,
     #email_error=email_error)
app.run()