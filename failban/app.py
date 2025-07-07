from flask import Flask, request, render_template, redirect, session
import logging, random, os


app = Flask(__name__)
app.secret_key = 'DAVIDBOMBAL'

log_path = "/var/log/app/app.log"
logging.basicConfig(filename=log_path, level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def login():
    num1, num2 = random.randint(1, 9), random.randint(1, 9)
    captcha_result = num1 + num2

    if request.method == 'POST':
        ip = request.remote_addr
        user = request.form['username']
        password = request.form['password']
        captcha = request.form.get('captcha')
        expected = request.form.get('expected')

        if str(captcha) != expected:
            return render_template('login.html', error='CAPTCHA salah', num1=num1, num2=num2, expected=captcha_result)

        if user == 'alex' and password == 'admin123':
            session['admin'] = True
            return redirect('/admin')
        else:
            logging.info(f"Failed login attempt user={user} ip={ip}")
            return render_template('login.html', error='Login gagal', num1=num1, num2=num2, expected=captcha_result)

    return render_template('login.html', num1=num1, num2=num2, expected=captcha_result)

@app.route('/admin')
def admin():
    if not session.get('admin'):
        return redirect('/')
    return render_template('admin.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

@app.route('/logs')
def logs():
    if not session.get('admin'):
        return redirect('/')
    
    app_log_path = "/var/log/app/app.log"
    fail2ban_log_path = "/var/log/fail2ban.log"

    app_log = ""
    fail2ban_log = ""

    if os.path.exists(app_log_path):
        with open(app_log_path, 'r') as f:
            app_log = f.read()[-5000:]  # baca 5000 karakter terakhir

    if os.path.exists(fail2ban_log_path):
        with open(fail2ban_log_path, 'r') as f:
            fail2ban_log = f.read()[-5000:]  # baca 5000 karakter terakhir

    return render_template('logs.html', app_log=app_log, fail2ban_log=fail2ban_log)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88, debug=True)

