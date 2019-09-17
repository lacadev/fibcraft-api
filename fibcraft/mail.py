import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from werkzeug.security import generate_password_hash
from flask import current_app, g, url_for


def get_mail_client():
    if "mail_client" not in g:
        g.mail_client = SendGridAPIClient(current_app.config["SENDGRID_API_KEY"])

    return g.mail_client


def send_mail(to: str, subject: str, msg: str):
    sg = get_mail_client()
    message = Mail(
        from_email=current_app.config["MAIL_FROM"],
        to_emails=to,
        subject=subject,
        html_content=msg,
    )
    response = sg.send(message)
    current_app.logger.info(response)
    return response

# TODO: Put an expiration date to the link (check day of registration in DB)

def send_verification_mail(to: str):
    hashed_mail = generate_password_hash(to)
    verification_url = f"http://{current_app.config['DOMAIN']}{url_for('signup.verify')}?token={hashed_mail}"
    subject = "FIBCRAFT Verification"
    msg = (
        "Hi there you pretty pie! So we've been told you want to join FIBCRAFT."
        " Awesome news!\nPlease go to the following url and you'll be whitelisted:\n"
        f"{verification_url}"
    )
    response = send_mail(to, subject, msg)
