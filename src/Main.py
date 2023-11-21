from flask import Flask

# Main instance of Flask app
app = Flask(__name__)

# Blueprint imports
from auth import auth

# Registering blueprints
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(user, url_prefix="/User")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)