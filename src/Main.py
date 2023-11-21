from flask import Flask

# Main instance of Flask app
app = Flask(__name__)

# Blueprint imports
from info import info

# Registering blueprints
app.register_blueprint(info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5502)