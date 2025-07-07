from flask import Flask, request, make_response, send_from_directory, render_template_string, redirect, url_for
import threading
import time
import requests

app = Flask(__name__)

FLAG = "alx{flag}"  # Ini flag-nya

@app.route('/')
def index():
    name = request.cookies.get('name', 'Guest')
    
    # Kalau admin yang buka dan detect FLAG_TRIGGER, tampilin flag
    if name == 'FLAG_TRIGGER':
        return f"<h1>🎉 Selamat! Ini flag mu: {FLAG}</h1>"

    return render_template_string(f"""
    <h1>Welcome {name}!</h1>
    <p><a href="/game">Play the game</a></p>
    <form action="/submit" method="post">
        <input type="text" name="name" placeholder="Enter your name">
        <input type="hidden" name="score" value="100">
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/game')
def game():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/submit', methods=['POST'])
def submit():
    score = request.form.get('score', '0')
    name = request.form.get('name', 'Guest')

    resp = make_response(render_template_string(f"""
    <h1>Thanks, {name}!</h1>
    <p>Your score: {score}</p>
    <a href="/">Back to Home</a>
    """))
    
    # Save nama ke cookie (vuln disini)
    resp.set_cookie('name', name)
    
    # Trigger admin visit otomatis setelah submit
    threading.Thread(target=visit_as_admin).start()
    
    return resp

def visit_as_admin():
    time.sleep(3)  # delay supaya server siap
    try:
        
        requests.get('http://localhost:57/', cookies={'name': 'FLAG_TRIGGER'}, timeout=5)
    except:
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=57,debug=True)

