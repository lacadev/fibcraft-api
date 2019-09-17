# fibcraft
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
