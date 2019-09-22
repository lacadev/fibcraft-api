import functools

from datetime import datetime, timedelta
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.security import check_password_hash

from api.db import get_db
from api.mail import send_verification_mail
from api.mc import whitelist


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
            send_verification_mail(email)
            db.execute(
                "INSERT INTO user (email, username, joiningDate, verified) VALUES (?, ?, ?, ?)",
                (email, username, datetime.now(), 0),
            )
            db.commit()
            msg = f"{username} for {email} registered successfully!"
            flash(msg)
            current_app.logger.info(msg)

            return redirect(url_for("signup.register"))

        flash(error, "error")
        current_app.logger.error(f"{error} - {email} -> {username}")

    return render_template("signup/register.html", title="FIBCRAFT Signup")


@bp.route("/verification/", methods=("GET", "POST"))
def verify():
    if request.method == "POST":
        hashed_mail = request.form["token"]
        plain_mail = request.form["email"]
        error = None

        if not check_password_hash(hashed_mail, plain_mail):
            error = f"Wrong verification email or URL"
        else:
            db = get_db()
            user = db.execute(
                "SELECT * FROM user WHERE email = ?", (plain_mail,)).fetchone()

            if user is None:
                error = f"The email address {plain_mail} is not registered"
                flash(error, "error")
            else:
                time_since_reg = datetime.now() - user["joiningDate"]
                if time_since_reg > timedelta(days=1):
                    db.execute("DELETE FROM user WHERE email=?", (plain_mail,))
                    db.commit()
                    current_app.logger.info(f"{plain_mail} deleted from the DB")
                    error = f"It has been more than 1 day since you registered. Please, register again"

            if error is None:
                current_app.logger.info(f"{plain_mail} has been verified")
                resp = whitelist(user["username"])
                db.execute("UPDATE user SET verified=? WHERE email=?", (1, plain_mail))
                db.commit()
                current_app.logger.info(f"{plain_mail} : {user['username']} - whitelisted")
                msg = f"Your email address has been verified successfully!"
                flash(msg)

        if error is not None:
            flash(error, "error")

        return redirect(url_for("signup.register"))

    return render_template("signup/verification.html", title="FIBCRAFT Verification")
