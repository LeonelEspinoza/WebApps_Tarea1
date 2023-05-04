from flask import Flask, render_template

app = Flask(__name__)

#http://localhost

#Rutas de nuestra app
#http://localhost/
@app.route("/")
def index():
    return render_template("inicio.html")

#http://localhost/agregar-donacion
@app.route("/agregar-donacion")
def add_donation():
    return render_template("agregar-donacion.html")

#http://localhost/agregar-pedido
@app.route("/agregar-pedido")
def add_request():
    return render_template("agregar-pedido.html")

#http://localhost/ver-donaciones
@app.route("/ver-donaciones")
def donations():
    return render_template("ver-donaciones.html")

#http://localhost/ver-pedidos
@app.route("/ver-pedidos")
def requests():
    return render_template("ver-pedidos.html")

#http://localhost/login
@app.route("/login")
def login():
    pass