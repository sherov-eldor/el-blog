from flask import render_template

def base_controller():
    return render_template('index.html')