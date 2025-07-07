FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install flask

EXPOSE 2365
CMD ["python", "app.py"]

