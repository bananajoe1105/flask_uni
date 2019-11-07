from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/counter')
def show_counter():
    return render_template("counter.html")

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/FlaskTutorial', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        return render_template('success.html', email=email)
    else: 
        pass 

@app.route('/start')
def count_higher():
   for i in range(10):
       return str(i)

if __name__ == "_main_":
    app.run()