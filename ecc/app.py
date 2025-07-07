from flask import Flask, render_template, request
import subprocess
import os
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_command():
    cmd = request.form.get('cmd', '')

    blocked = ['cat','flag','more','less','nano','vim','tail','head']
    if any(word in cmd.lower() for word in blocked):
        return "Command Not Found."
    # VULNERABLE TO COMMAND INJECTION
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=3, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    except Exception as e:
        output = str(e)

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2628,debug=True)
