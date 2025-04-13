from flask import Flask, render_template, request
from app.routes.main.mainRoutes import mainBp


def create_app():
    app = Flask(__name__)

    # Routes
    app.register_blueprint(mainBp)

    return app
