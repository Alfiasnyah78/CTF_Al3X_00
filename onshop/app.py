from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'onepiece-secret'

# Buat DB & user dummy
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute('INSERT OR IGNORE INTO users VALUES (1, "admin", "santet123")')
    c.execute('INSERT OR IGNORE INTO users VALUES (2, "zoro", "katana")')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        # Rawan SQLi!
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Running query:", query)
        c.execute(query)
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]
            session['role'] = 'admin' if user[1] == 'admin'else 'user'
            return redirect('/')
        else:
            return "<h3>Login gagal!</h3><a href='/login'>Coba lagi</a>"

    return render_template("login.html")

@app.route('/profile/<int:uid>')
def profile(uid):
    profiles = {
        1: {"name": "Monkey D. Luffy", "email": "luffy@onepiece.com"},
        2: {"name": "Zoro", "email": "lato-lato@onepiece.com"},
        3: {"name": "Nami", "email": "namikazo@onepiece.com"},
        4: {"name": "sanji", "email": "sanji123@onepiece.com"},
        5: {"name": "Nico Robin", "email": "robin@onepiece.com", "flag": "alx{ID0R42h_hHuiriken41_basf62}"}
    }

    profile = profiles.get(uid)
    if not profile:
        return "Profile not found!", 404

    user_role = session.get("role", "guest")

    # IDOR logic: user bisa akses profile 1, admin bisa akses 2
    if uid == 5 and user_role != "admin":
        return "Unauthorized: kamu bukan admin!", 403

    return render_template("profile.html", profile=profile, id=uid)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Route order (tidak diubah dari sebelumnya)
@app.route('/order/<int:order_id>')
def view_order(order_id):
    orders = {
        1: {"name": "Luffy", "item": "Topi Jerami", "price": "$10"},
        2: {"name": "Zoro", "item": "Pedang Wado Ichimonji", "price": "$300"},
        3: {"name": "Sanji", "item": "Sepatu Hitam", "price": "$120"},
        4: {"name": "Nami", "item": "Sepatu Hitam", "price": "$120"},
        5: {"name": "Chopper", "item": "Sepatu Hitam", "price": "$120"},
        7: {"name": "Jinbe", "item": "Sepatu Hitam", "price": "$120"}, 
        9: {"name": "Robin", "item": "Sepatu Hitam", "price": "$120"},
        10: {"name": "Brook", "item": "Sepatu Hitam", "price": "$120"},
        11: {"name": "Usop", "item": "Sepatu Hitam", "price": "$120"},
        12: {"name": "Franky", "item": "Sepatu Hitam", "price": "$120"},
    }
    order = orders.get(order_id)
    if not order:
        return "Order not found!", 404
    return render_template("order.html", order=order, id=order_id)

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=40, debug=True)

