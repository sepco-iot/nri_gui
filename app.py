from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__, static_url_path='/static')



@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if request.form['submit'] == 'E-Meter':
            return redirect(url_for('emeterpage'))
    return render_template("homepage.html")


@app.route('/emeter')
def emeterpage():
    return render_template('emeter.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    #app.run(host='localhost', port=5000, debug=True)
    app.run()








