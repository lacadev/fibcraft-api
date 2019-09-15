import functools

from datetime import datetime
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from fibcraft.db import get_db


bp = Blueprint("signup", __name__, url_prefix="/signup")


@bp.route("/", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        db = get_db()
        error = None

        if not email:
            error = "Email is required"
        elif email.split("@")[1] != "est.fib.upc.edu":
            error = "Email must be from FIB"
        elif not username:
            error = "Minecraft username is required"
        elif (
            db.execute(
                "SELECT id FROM user WHERE email = ? OR username = ?", (email, username)
            ).fetchone()
            is not None
        ):
            error = "Minecraft username or FIB email already in use"

        if error is None:
            db.execute(
                "INSERT INTO user (email, username, joiningDate) VALUES (?, ?, ?)",
                (email, username, datetime.now()),
            )
            db.commit()
            msg = f"{username} for {email} registered successfully!"
            flash(msg)
            current_app.logger.info(msg)
            return redirect(url_for("signup.register"))

        flash(error, "error")
        current_app.logger.error(f"{error} - {email} -> {username}")

    return render_template("signup/register.html")
