FROM python:3.11-slim

WORKDIR /app

COPY . /app
RUN pip install flask pyjwt

EXPOSE 5872

CMD ["python", "app.py"]

