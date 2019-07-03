from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/electricity_meter')
def electricity_meter_page():
    return render_template('electricity_meter.html')

@app.route('/water_meter')
def water_meter_page():
    return render_template('water_meter.html')

@app.route('/street_light')
def street_light_page():
    return render_template('street_light.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='192.168.55.81', port=5000, debug=False)
    # app.run()
    #  app.run(host='localhost', port=5000, debug=False)








