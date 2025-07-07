from flask import Flask, request, render_template_string, send_file
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{dummy_flag}")

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        user_input = request.form.get("message", "")
        try:
            template = """{% raw %}<div class='msg-box'>Your Message:<br>""" + user_input + """</div>{% endraw %}"""
            rendered = render_template_string(template)
            return rendered
        except Exception as e:
            return f"Error rendering template: {e}"
    return open("templates/index.html").read()

@app.route('/static/<path:path>')
def send_static(path):
    return send_file(f'static/{path}')

