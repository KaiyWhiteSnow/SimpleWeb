from flask import Blueprint, request, jsonify
from ..Database.Database import Session, func
from ..Database.models.Models import Users

auth = Blueprint("auth", __name__)

SessionInstance = Session()

@auth.route("/register", methods=['POST'])
async def register():
    return jsonify(["Request failure: " "I broke"])