from flask import Blueprint, request, jsonify, render_template
from Database.Database import Session, func
from Database.models.Models import example

info = Blueprint("info", __name__)

SessionInstance = Session()

@info.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@info.route("/join", methods=["POST", "GET"])
def about():
    return render_template("join.html")


@info.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")