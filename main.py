from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST", "GET"])
def index():
    encoded_error = request.args.get("error")
    
    return render_template('sign-in.html', error=encoded_error)

@app.route("/welcome.html", methods=['POST'])
def welcome():
    username = str(request.form.get('username'))
    password = str(request.form.get('pword'))
    verified_password = str(request.form.get('verpword'))
    email = str(request.form.get('email'))
    list_email = list(email)

    if username.isalnum() == False:
        user_error = "Username cannot contain spaces."
        return redirect("/?error=" + user_error)
    if len(username) < 3:
        user_error = "That username is too short"
        return redirect("/?error=" + user_error)
    if len(username) > 20:
        user_error = "That username is too long"
        return redirect("/?error=" + user_error)
    if password.isalnum() == False:
        pw_error = "Password cannot contain spaces."
        return redirect("/?error=" + pw_error)
    if len(password) < 3:
        pw_error = "That password is too short"
        return redirect("/?error=" + pw_error)
    if len(password) > 20:
        pw_error = "That password is too long"
        return redirect("/?error=" + pw_error)
    if verified_password != password:
        vpw_error = "Passwords do not match"
        return redirect("/?error=" + vpw_error)
    if email != '':
        if len(email) < 3:
            email_error = "That email is too short"
            return redirect("/?error=" + email_error)
        if len(email) > 20:
            email_error = "That email is too long"
            return redirect("/?error=" + email_error)
        if ('@' not in list_email) == True and ('.' not in list_email) == True:
            email_error = "Not a valid email"
            return redirect('/?error=' + email_error)

    return render_template('welcome.html', username = username)
app.run()