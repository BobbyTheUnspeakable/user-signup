from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST", "GET"])
def index():
    encoded_error = request.args.get("error")
    #username = str(request.form.get('username'))
    #if len(username) < 3:
    #    error = "That username is too short"
    #    return redirect("/?error=" + error)
    #if len(username) > 20:
    #    error = "That username is too long"
    #    return redirect("/?error=" + error)
    #password = request.form.get('pword')
    #verified_password = request.form.get('verpword')
    #email = request.form.get('email')
    return render_template('sign-in.html', error=encoded_error)

@app.route("/welcome.html", methods=['POST'])
def welcome():
    username = str(request.form.get('username'))
    for char in username:
        if char == '':
            error = "Username cannot contain spaces."
            return redirect("/?error=" + error)            )
    if len(username) < 3:
        error = "That username is too short"
        return redirect("/?error=" + error)
    if len(username) > 20:
        error = "That username is too long"
        return redirect("/?error=" + error)
    password = request.form.get('pword')
    verified_password = request.form.get('verpword')
    email = request.form.get('email')
    return render_template('welcome.html')
app.run()