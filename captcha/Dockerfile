FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY templates/ templates/
COPY static/ static/
COPY static/robots.txt /app/robots.txt

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 43

CMD ["python", "app.py"]

