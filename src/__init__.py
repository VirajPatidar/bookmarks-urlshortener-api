from flask.json import jsonify
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from flask import Flask, config, redirect, render_template
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db, Bookmark
from flask_jwt_extended import JWTManager


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),
        )

    else:
        app.config.from_mapping(test_config)


    db.app = app
    db.init_app(app)


    JWTManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)


    @app.get("/")
    def index():
        return "Hello World"

    @app.get("/hello")
    def say_hello():
        return jsonify({"message": "Hello World"})

    @app.route("/hw")
    def template_test():
        return render_template('hello.html', my_string="Hello World !", my_list=[0,1,2,3,4,5])


    return app