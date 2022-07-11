from flask import Blueprint, render_template, redirect

views = Blueprint('views', __name__)

@views.route('/<name>')
def home(name):
    return render_template("home.html", name=name)
