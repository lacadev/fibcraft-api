from mcrcon import MCRcon
from flask import current_app, g


def rcon_context(cmd):
    if "rcon" not in g:
        g.rcon = MCRcon(current_app.config["RCON_IP"], current_app.config["RCON_PASSWORD"])

    with g.rcon as mcr:
        return mcr.command(cmd)


def whitelist(username):
    return rcon_context(f"whitelist add {username}")
