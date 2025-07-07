# Dockerfile
FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y python3 python3-pip fail2ban supervisor && \
    mkdir -p /var/log/fail2ban /var/log/app

# Install Flask
RUN pip3 install flask

# Add app files
COPY app.py /app/app.py
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY jail.local /etc/fail2ban/jail.local
COPY filter.d/ /etc/fail2ban/filter.d/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Make sure log file exists
RUN touch /var/log/app/app.log

WORKDIR /app

CMD ["/usr/bin/supervisord"]

