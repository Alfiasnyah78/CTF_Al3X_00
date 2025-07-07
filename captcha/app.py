from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import send_from_directory

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

FLAG = "alx{flag}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        nama = request.form.get("nama", "")
        captcha = request.form.get("captcha", "").strip()
        if captcha != "7":
            result = "CAPTCHA salah."
        elif nama.lower() == "sysadmin123":
            result = FLAG
        else:
            result = f"Halo, {nama}!"
    return render_template("index.html", result=result)

@app.route("/robots.txt")
def robots():
    return send_from_directory(".", "robots.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=43, debug=True)

