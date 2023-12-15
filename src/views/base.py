from flask import render_template

def base_controller():
    active_page_name = 'home'
    return render_template('home.html', page_name=active_page_name)