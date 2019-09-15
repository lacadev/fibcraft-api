FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn
ENTRYPOINT ["/app/run.sh"]
