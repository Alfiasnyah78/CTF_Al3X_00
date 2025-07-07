from flask import Flask, render_template
from flask import request
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    try:
        # command injection vulnerability (simulasi)
        command = f"echo {username} && cat flag.txt && echo {password}"
        result = os.popen(command).read()
        return f"<pre>{result}</pre>"
    except Exception as e:
        return f"<pre>Error: {e}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)

