from flask import Blueprint

userBlue = Blueprint("userBlue", __name__)


@userBlue.route("/")
def user():
    return "userView"
