from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from storms-burrow import app

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/orderstorm')
def orderstorm():
    return render_template('orderstorm.html')

@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] != 'admin':
            flash('Invalid Password')
    return redirect('/orderstorm')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/teachings')
def teachings():
    return render_template('teachings.html')

@app.route('/our_teachings')
def our_teachings():
    return render_template('our_teachings.html')

@app.route('/storm')
def storm():
    return render_template('storm.html')

@app.route('/join')
def join():
     return redirect("https://discord.gg/znAubK35zN")

