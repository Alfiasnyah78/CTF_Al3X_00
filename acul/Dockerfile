FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install flask

# Copy flag.txt to root
RUN cp flag.txt /flag.txt

EXPOSE 5654

CMD ["python", "app.py"]

