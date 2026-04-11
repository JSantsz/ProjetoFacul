from flask import Flask, request, jsonify, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "segredo"

def conectar():
    return sqlite3.connect("clinica.db")


# HOME

@app.route("/")
def home():
    return render_template("home.html")


# LOGIN PAGE

@app.route("/login")
def login_page():
    return render_template("login.html")

# CADASTRO

@app.route("/register", methods=["POST"])
def register():
    data = request.form

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                   (data["nome"], data["email"], data["senha"]))

    conn.commit()
    conn.close()

    return redirect("/login")

# LOGIN

@app.route("/login", methods=["POST"])
def login():
    data = request.form

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?",
                   (data["email"], data["senha"]))

    user = cursor.fetchone()
    conn.close()

    if user:
        session["user_id"] = user[0]
        session["nome"] = user[1]
        return redirect("/dashboard")
    else:
        return "Login inválido"

# DASHBOARD (PACIENTE)

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect ("/login")
    
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT medico,data,hora FROM consultas WHERE usuario_id=?",
                   (session["user_id"],))
    
    consultas = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", nome=session["nome"], consultas=consultas)

# LOGOUT

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# ROTA DE AGENDAMENTO

@app.route("/agendar", methods=["POST"])
def agendar():
    if "user_id" not in session:
        return redirect("/login")
    
    data = request.form

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO consultas (usuario_id, medico, data, hora)
            VALUES (?,?,?,?)
            """, (session["user_id"], data["medico"], data["data"], data["hora"]))
    
    conn.commit()
    conn.close()

    return redirect("/dashboard")