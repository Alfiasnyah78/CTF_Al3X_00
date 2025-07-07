from flask import Flask, request, render_template, render_template_string, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key_for_ssti_lab"

FLAG = "alx{tipu-tipu}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("input")
        try:
            result = render_template_string(user_input)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        # Login sukses kalau username = admin (tidak dicek password)
        if username == "admin":
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            return render_template("login.html", error="Login gagal")
    return render_template("login.html")

@app.route("/admin")
def admin():
    if not session.get("admin"):
        return "Kamu bukan admin!"
    return render_template("admin.html", flag=FLAG)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

