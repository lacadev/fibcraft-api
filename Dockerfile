FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fibcraft:create_app()"]
