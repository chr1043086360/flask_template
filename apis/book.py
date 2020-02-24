from flask import Blueprint

bookBlue = Blueprint("bookBlue", __name__)


@bookBlue.route("/list")
def list():
    return "bookBlue"