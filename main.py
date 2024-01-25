from flask import Blueprint,render_template


main = Blueprint('main',__name__) # Blueprint is the way to organize the file in flask project

@main.route('/')
def index():
    return render_template('index.html')

@main.route("/profile")
def profile():
    return "Profile"

@main.route("/user_workouts")
def user_workouts():
    return 'ok'



