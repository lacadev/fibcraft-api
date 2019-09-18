# FIBCraft [WIP] :pick:
### Current status
Missing whitelisting in realtime and adding those sweet plugins
## What
This is a minecraft server for students at FIB! That's about it really... No wait, there's more.
So the project is made out of your usually dockerized Minecraft server AAAND a website to, wait for it, register the Minecraft username you we'll use with your FIB email!

That's right, that means the server has whitelisting. Only FIB students allowed, now that's what I call exclusivity. To accomplish that, once you submit the username and FIB email address, you'll receive an email from FIBCraft to verify your account. Click on the URL you'll be given and BOOM, you done vro. You are now able to join the server.

You know what that means too right? No? K lemme spell it out for ya. Because of the email verification, each person will only be able to join the server with one username so... no need to make the server premium to ensure that! That's right baby, you got an illegal copy of Minecraft? We got you covered! THIS SERVER IS **NOT PREMIUM**. I mean, you can still join with a premium account of course. In fact, we encourage that, let's support the devs :D

Btw, _premium_ means having a legal (bought) copy of the game. For a server that means only allowing people that have bought the game. But we are students, we are broke, so none of that.

## You wanna host this yourself? Ight
### Requirements
Not much really:
- Sendgrid API set up
- Custom domain
- Server to host this thing
- LOTS OF RAM AND CPU FOR ALL THE PEOPLE THAT WILL JOIN THE SERVER AM I RIGHT?

### Procedure
- Create a `.env` file in the root directory of the project and put inside the required environment variables:
```bash
FLASK_APP=fibcraft
SECRET_KEY=XXXXXXXXXXXXXXXX
SENDGRID_API_KEY=XXXXXXXXXXXXXXX
DOMAIN=exampledomain.com
MAIL_FROM=example@something.com
```
_To randomly generate a new secret key:_
```bash
python -c "import os; print(os.urandom(16))"
```
- Make sure ports 80 and 25565 are available (looking at you firewall):
- Finally, run:
```bash
docker-compose up
```
