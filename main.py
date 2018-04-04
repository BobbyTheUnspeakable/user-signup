from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    sign_in = request.form('sign-in.html')
    return render_template('sign-in.html')

app.run()