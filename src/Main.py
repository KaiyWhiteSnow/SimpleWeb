from flask import Flask

# Main instance of Flask app
app = Flask(__name__)

# Blueprint imports
from info import info

# Registering blueprints
app.register_blueprint(info)