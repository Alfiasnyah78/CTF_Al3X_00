from flask import Flask, request, redirect, make_response, render_template, send_from_directory
import jwt  # PyJWT
import datetime
import os
import json
import base64  # << penting untuk decoding manual

app = Flask(__name__)
SECRET_KEY = "super-secret-dont-share-alex-nfscc"

users = {
    "admin": "admI823jashdu$#@",
    "user": "jwttokenbro"
}

FLAG = "alx{JwT_T0k3Nn_Broken_Access_Control}"

def generate_token(username, role):
    payload = {
        "user": username,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        if u in users and users[u] == p:
            role = "admin" if u == "admin" else "user"
            token = generate_token(u, role)
            resp = make_response(redirect("/dashboard"))
            resp.set_cookie("token", token)
            return resp
        return "Login failed", 403
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    token = request.cookies.get("token")
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return render_template("dashboard.html", username=data["user"], role=data["role"])
    except Exception:
        return redirect("/")

@app.route("/admin")
def admin():
    token = request.cookies.get("token")
    if not token:
        return redirect("/")
    try:
        header_b64, payload_b64, signature_b64 = token.split(".")

        def pad(b64): return b64 + "=" * (-len(b64) % 4)

        payload_json = base64.urlsafe_b64decode(pad(payload_b64)).decode()
        data = json.loads(payload_json)

        if data.get("role") != "admin":
            return "Unauthorized", 403

        return render_template("admin.html", flag=FLAG)
    except Exception as e:
        return f"Token Error: {str(e)}", 400

@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    resp.set_cookie("token", "", expires=0)
    return resp

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5872)

