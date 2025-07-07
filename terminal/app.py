from flask import Flask, request, render_template, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import subprocess, re, datetime

app = Flask(__name__)
auth = HTTPBasicAuth()

# User database
users = {
    "onepiece": generate_password_hash("gomugomuno")
}

# Command patterns to block (regex)
BLOCKED_PATTERNS = [
    r"\brm\b", r"\bshutdown\b", r"\breboot\b", r"\bmkfs\b", r"\bdd\b",
    r"\bpoweroff\b", r"\bwget\b", r"\bcurl\b", r"\bscp\b", r":\(\)\s*{\s*:.*};",
    r"[;&|><`]",  # shell injection
]

# Auth check
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

# Check if command is safe
def is_command_safe(command):
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            return False
    return True

# Log commands
def log_command(user, cmd):
    with open("command_log.txt", "a") as log:
        log.write(f"[{datetime.datetime.now()}] {user} >> {cmd}\n")

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
@auth.login_required
def run():
    cmd = request.json.get('command')
    cwd = session.get('cwd', os.path.expanduser("~"))
    log_command(auth.current_user(), cmd)

    # Handle 'cd' khusus
    if cmd.startswith("cd "):
        target = cmd[3:].strip()
        target_path = os.path.abspath(os.path.join(cwd, target))
        if os.path.exists(target_path) and os.path.isdir(target_path):
            session['cwd'] = target_path
            return jsonify({"output": ""})
        else:
            return jsonify({"output": f"bash: cd: {target}: No such directory"})

    # Cek perintah terlarang
    if not is_command_safe(cmd):
        return jsonify({"output": "[ERROR] Command is blocked for safety."})

    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True)
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)

    return jsonify({
        "output": output,
        "cwd": session.get('cwd', '~'),
        "user": auth.current_user(),
        "host": "localhost"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=638)

