# fibcraft
Create a `.env` file in the root directory of the project and put inside the required environment variables:
```
FLASK_APP=fibcraft
SECRET_KEY=XXXXXXXXXXXXXXXX
```
_To randomly generate a new secret key:_
```
python -c "import os; print(os.urandom(16))"
```
Finally, run:
```
docker-compose up
```
