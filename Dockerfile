FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn sendgrid
ENTRYPOINT ["/app/run.sh"]
