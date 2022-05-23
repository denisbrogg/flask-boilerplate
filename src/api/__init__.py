from flask import Flask
from api.routes import circle_blueprint


def create_app() -> Flask:
    
    # Create flask app
    app = Flask(__name__)

    # Register routes
    app.register_blueprint(circle_blueprint, url_prefix='/circle')

    # Add simple page that says hello
    @app.route('/')
    def hello():
        return "Flask is up and running!"

    # Return

    return app