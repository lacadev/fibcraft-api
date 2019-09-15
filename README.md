# fibcraft
RUN:
```
docker build -t fibcraft .
docker run --rm --name fibcraft -p 80:8000 --env SECRET_KEY=abcd fibcraft
```
