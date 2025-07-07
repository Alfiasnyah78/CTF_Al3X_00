from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/")
def dashboard():
    hosts = [f.replace(".json", "") for f in os.listdir(LOG_DIR) if f.endswith(".json")]
    return render_template("dashboard.html", hosts=hosts)

@app.route("/logs/<host>")
def view_log(host):
    filepath = os.path.join(LOG_DIR, f"{host}.json")
    try:
        with open(filepath) as f:
            lines = f.readlines()
        logs = [json.loads(line) for line in lines if line.strip()]
    except Exception as e:
        logs = []
    return render_template("logs.html", host=host, logs=logs)

@app.route("/upload", methods=["POST"])
def upload():
    host = request.form.get("host")
    file = request.files.get("log")
    if host and file:
        file.save(os.path.join(LOG_DIR, f"{host}.json"))
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=93, debug=True)

