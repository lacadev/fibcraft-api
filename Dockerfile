FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn sendgrid mcrcon
ENTRYPOINT ["/app/run.sh"]
