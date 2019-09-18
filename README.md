# FIBCraft :pick:
## What
This is a minecraft server for students at FIB! That's about it really... No wait, there's more.
So the project is made out of your usually dockerized Minecraft server AAAND an website to, wait for it, register the Minecraft username you we'll use with your FIB email!

That's right, that means the server has whitelisting. Only FIB students allowed, now that's what I call exclusivity. To accomplish that, once you submit the username and FIB email address, you'll receive an email from FIBCraft to verify your account. Click on the URL you'll be given and BOOM, you done vro. You are now able to join the server.

You know what that means too right? No? K lemme spell it out for ya. Because of the email verification, each person will only be able to join the server with one username so... no need to make the server premiumto ensure that! That's right baby, you got an illegal copy of Minecraft? We got you covered! THIS SERVER IS **NOT PREMIUM**. I mean, you can still join with a premium account of course. In fact, we encourage that, let's support the devs :D

Btw, _premium_ means having a legal (bought) copy of the game. For a server that means only allowing people that have bought the game. But we are students, we are broke, so none of that.



Create a `.env` file in the root directory of the project and put inside the required environment variables:
```
FLASK_APP=fibcraft
SECRET_KEY=XXXXXXXXXXXXXXXX
SENDGRID_API_KEY=XXXXXXXXXXXXXXX
DOMAIN=exampledomain.com
MAIL_FROM=example@something.com
```
_To randomly generate a new secret key:_
```
python -c "import os; print(os.urandom(16))"
```
Finally, run:
```
docker-compose up
```
