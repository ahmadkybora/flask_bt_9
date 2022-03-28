from Models.User import User
from flask import render_template

class UserController():
    # def __init__(self):
    #     self
        
    def index():
        users = User.query.all()
        return render_template("home.html", users = users)