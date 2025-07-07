from flask import Flask, render_template_string, request
import re

app = Flask(__name__)

# Template dasar
template = """
<!DOCTYPE html>
<html>
<head><title>SSTI Output</title></head>
<body style="background-color:black;color:#00ff99;font-family:'Share Tech Mono',monospace;padding:2rem">
<h2>>> Output:</h2>
<p>{{ user_input }}</p>
<a href="/" style="color:#00ffaa">← Kembali</a>
</body>
</html>
"""

# Filter sederhana untuk cegah eksploitasi langsung
def sanitize_input(user_input):
    # Blok tag atau karakter mencurigakan
    blacklist = [
        r"\{\{", r"\}\}", r"request", r"config", r"self", r"class", r"mro",
        r"__.*?__", r"os", r"import", r"eval", r"subprocess", r"popen",
        r"globals", r"locals", r"exec"
    ]
    for pattern in blacklist:
        user_input = re.sub(pattern, "[BLOCKED]", user_input, flags=re.IGNORECASE)
    return user_input

@app.route("/", methods=["GET"])
def index():
    return render_template_string(open("templates/index.html").read())

@app.route("/greet", methods=["POST"])
def greet():
    user_input = request.form.get("name", "")
    sanitized_input = sanitize_input(user_input)
    return render_template_string(template, user_input=sanitized_input)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

