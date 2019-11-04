from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<counter>')
def show_counter(counter):
    return render_template("counter.html", counter=counter)

@app.route('/login')
def index():
    return render_template('login.html')