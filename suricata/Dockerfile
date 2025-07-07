FROM python:3.9-slim

RUN pip install flask

WORKDIR /app
COPY app.py .
COPY templates/ templates/
COPY static/ static/

EXPOSE 93

CMD ["python", "app.py"]

