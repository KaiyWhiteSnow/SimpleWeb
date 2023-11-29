from flask import Blueprint, request, jsonify, render_template
from Database.Database import Session, func
from Database.models.Models import example

info = Blueprint("info", __name__)

SessionInstance = Session()

@info.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@info.route("/join", methods=["GET"])
def join():
    return render_template("join.html")

@info.route("/faq", methods=["GET"])
def faq():
    return render_template("faq.html")