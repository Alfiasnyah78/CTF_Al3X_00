from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)

def is_suspicious(command):
    # Cek karakter-karakter umum yang dipakai untuk command injection
    blacklist = [';', '&', '|','`', '$(', ')', '>', '<']
    return any(char in command for char in blacklist)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hack', methods=['POST'])
def hack():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # Cek input user (tapi bisa diakali dengan teknik bypass sederhana)
    if is_suspicious(username) or is_suspicious(password):
        return "🚨 Command injection terdeteksi! Jangan nakal ya :)"

    # Tetap ada celah kalau user pintar
    result = os.popen(f"echo {username}:{password} >> logs.txt && cat flag.txt").read()
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000, debug=True)

