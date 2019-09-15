import os

from flask import Flask, redirect, url_for

from . import db
from . import signup


SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, "fibcraft.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.logger.setLevel("INFO")

    db.init_app(app)

    app.register_blueprint(signup.bp)

    @app.route("/")
    def index():
        return redirect(url_for("signup.register"))

    return app
