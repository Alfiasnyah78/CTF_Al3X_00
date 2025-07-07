# app.py (versi ditingkatkan dengan UI keren, autentikasi, dan Google Maps)
from flask import Flask, render_template, request, redirect, url_for, session
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Dummy credentials (ganti dengan yang aman di produksi)
USERS = {
    "alexkece": "lol#123#"
}


def lookup_number(number):
    try:
        parsed_number = phonenumbers.parse(number)
        location = geocoder.description_for_number(parsed_number, 'id')
        provider = carrier.name_for_number(parsed_number, 'id')
        timezones = timezone.time_zones_for_number(parsed_number)

        api_key = ""  # Isi dengan API key Numverify jika ada
        additional_info = {}
        if api_key:
            url = f"http://apilayer.net/api/validate?access_key={api_key}&number={number}"
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                additional_info = {
                    "country": data.get("country_name"),
                    "location": data.get("location"),
                    "line_type": data.get("line_type"),
                    "carrier_api": data.get("carrier"),
                    "lat": data.get("latitude"),
                    "lon": data.get("longitude")
                }

        return {
            "number": number,
            "location": location,
            "provider": provider,
            "timezones": timezones,
            "additional": additional_info
        }

    except Exception as e:
        return {"error": str(e)}


@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    result = None
    if request.method == "POST":
        number = request.form.get("phone")
        result = lookup_number(number)
    return render_template("index.html", result=result)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if USERS.get(username) == password:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Username atau password salah.")
    return render_template("login.html")


@app.route("/leak")
def leak():
    con = sqlite3.connect("users.db")
    c = con.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    con.close()

    table = "<h2>🔥 Dump isi users.db 🔥</h2><table border='1'><tr><th>ID</th><th>Username</th><th>Password</th></tr>"
    for row in rows:
        table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
    table += "</table>"

    return table

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        users = load_users()
        if username in users:
            return render_template("login.html", error="Username sudah digunakan.") #ya biasanya sih kalo kita namain apa ya kalo udah dapet database orang

        users[username] = password
        save_users(users)
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/comment", methods=["GET", "POST"])
def comment():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    comment = ""
    if request.method == "POST":
        comment = request.form.get("comment", "")
        # deteksi payload xss
        if "<script>" in comment or "alert(" in comment:
            session["show_flag"] = True
    
    if session.pop("show_flag", None): #hanya tampil sekali

            return render_template("comment.html", comment=comment)

@app.route("/flag")
def flag():
    # Cek agar hanya XSS dari sisi client yang bisa akses
    if not session.get("logged_in"):
        return "", 403
    return "alx{flag}"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6723, debug=True)
