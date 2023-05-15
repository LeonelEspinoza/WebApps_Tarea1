from flask import Flask, request, render_template, redirect, url_for
from utils.validations import validate_donation, validate_request
from db import db
app = Flask(__name__)

#http://localhost

#Rutas de nuestra app
#http://localhost/
@app.route("/")
def index():
    return render_template("inicio.html")

#http://localhost/agregar-donacion
@app.route("/agregar-donacion",  methods=('GET', 'POST'))
def add_donation():
    error = None
    if (request.method =='POST'):
        region = request.form['region']
        comuna = request.form['comuna']
        calle_numero = request.form['calle-numero']
        tipo_donacion = request.form['tipo-donacion']
        cantidad = request.form['cantidad']
        fecha = request.form['fecha']
        foto_donacion = request.files['foto-donacion']
        nombre = request.form['nombre']
        email = request.form['email']
        celular = request.form['celular']
        validation=validate_donation(region,comuna,calle_numero,tipo_donacion,cantidad,fecha,foto_donacion,nombre,email,celular)
        if (validation==[]):
            return redirect(url_for('index'))
        else:
            return render_template("forms/agregar-donacion.html", error=validation)
    return render_template("forms/agregar-donacion.html")

#http://localhost/agregar-pedido
@app.route("/agregar-pedido",  methods=('GET', 'POST'))
def add_request():
    if (request =='POST'):
        region = request.form['region']
        comuna = request.form['comuna']
        tipo_pedido = request.form['tipo-pedido']
        cantidad = request.form['cantidad']
        nombre = request.form['nombre']
        email = request.form['email']
        celular = request.form['celular']
        validation=validate_request(region,comuna,tipo_pedido,cantidad,nombre,email,celular)
        if (validation==[]):
            return redirect(url_for('index'))
        else:
            return render_template("forms/agregar-pedido.html", error=validation)
    return render_template("forms/agregar-pedido.html")

#http://localhost/ver-donaciones
@app.route("/ver-donaciones")
def donations():
    return render_template("tables/ver-donaciones.html")

#http://localhost/ver-pedidos
@app.route("/ver-pedidos")
def requests():
    return render_template("tables/ver-pedidos.html")

#http://localhost/informacion-donacion
@app.route("/informacion-donacion")
def donation_info():
    return render_template("specific_info/informacion-donacion.html")

#http://localhost/informacion-pedido
@app.route("/informacion-pedido")
def request_info():
    return render_template("specific_info/informacion-pedido.html")

if __name__ == "__main__":
    app.run(debug=True)