import os

from flask import Flask, redirect, url_for

from . import db
from . import signup


SECRET_KEY = os.environ.get("SECRET_KEY")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
API_DOMAIN = os.environ.get("API_DOMAIN")
MAIL_FROM = os.environ.get("MAIL_FROM")
RCON_IP = os.environ.get("RCON_IP")
RCON_PASSWORD = os.environ.get("RCON_PASSWORD")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")
if not SENDGRID_API_KEY:
    raise ValueError("No SENGRID_API_KEY set for Flask application")
if not API_DOMAIN:
    raise ValueError("No DOMAIN set for Flask application")
if not MAIL_FROM:
    raise ValueError("No MAIL_FROM set for Flask application")
if not RCON_IP:
    raise ValueError("No RCON_IP set for Flask application")
if not RCON_PASSWORD:
    raise ValueError("No RCON_PASSWORD set for Flask application")


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, "fibcraft.sqlite"),
        SENDGRID_API_KEY=SENDGRID_API_KEY,
        API_DOMAIN=API_DOMAIN,
        MAIL_FROM=MAIL_FROM,
        RCON_IP=RCON_IP,
        RCON_PASSWORD=RCON_PASSWORD,
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
