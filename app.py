from flask import Flask, request, render_template, redirect, url_for
from utils.validations import validate_donation, validate_request
from db import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'static/media/img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    #if POST
    if (request.method =='POST'):
        
        #get inputs
        region = request.form['region']
        comuna = request.form['comuna']
        calle_numero = request.form['calle-numero']
        tipo_donacion = request.form['tipo-donacion']
        cantidad = request.form['cantidad']
        fecha = request.form['fecha']
        descripcion = request.form['descripcion']
        condiciones_retiro = request.form['condiciones-retiro']
        foto_donacion = request.files['foto-donacion']
        nombre = request.form['nombre']
        email = request.form['email']
        celular = request.form['celular']
        
        #donation's validation
        validation=validate_donation(region,comuna,calle_numero,tipo_donacion,cantidad,fecha,foto_donacion,nombre,email,celular)
        
        #if donation valid
        if (validation==[]):
            #get comuna id ("15" and "Camarones" are a place holder)
            comuna_id=db.get_comuna_id("15", "Camarones")
            
            #save donation to database
            db.create_donation(comuna_id, calle_numero, tipo_donacion, cantidad, fecha, descripcion , condiciones_retiro , nombre, email, celular)
            
            #get img_filename = filename . extension
            _filename = hashlib.sha256(
                secure_filename(foto_donacion.filename).encode("utf-8")
            ).hexdigest()
            _extension = filetype.guess(foto_donacion).extension
            img_filename = f"{_filename}.{_extension}"

            # save img as a file
            foto_donacion.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
            
            #get donation_id
            donation_id = db.get_donation_id_by_values(comuna_id, calle_numero, tipo_donacion, cantidad, fecha, descripcion , condiciones_retiro , nombre, email, celular)

            #save donation photo to database
            db.insert_photo(app.config["UPLOAD_FOLDER"], img_filename, donation_id)

            return redirect(url_for('index'))
        #donation invalid
        else:
            return render_template("forms/agregar-donacion.html", error=validation)
    #GET
    return render_template("forms/agregar-donacion.html")

#http://localhost/agregar-pedido
@app.route("/agregar-pedido",  methods=('GET', 'POST'))
def add_request():
    error=None
    #if POST
    if (request.method =='POST'):
    
        #get inputs
        region = request.form['region']
        comuna = request.form['comuna']
        tipo_pedido = request.form['tipo-pedido']
        cantidad = request.form['cantidad']
        descripcion = request.form['descripcion']
        nombre = request.form['nombre']
        email = request.form['email']
        celular = request.form['celular']
    
        #request's validation
        validation=validate_request(region, comuna, tipo_pedido, cantidad, descripcion, nombre, email, celular)
        
        #if request valid
        if (validation==[]):
            #get comuna id ("15" and "Camarones" are a place holder)
            comuna_id=db.get_comuna_id("15", "Camarones")

            #save request to database
            db.create_request(comuna_id, tipo_pedido, descripcion, cantidad, nombre, email, celular)
            
            return redirect(url_for('index'))
    
        #request invalid
        else:
            return render_template("forms/agregar-pedido.html", error=validation)
    
    #GET
    return render_template("forms/agregar-pedido.html")

#http://localhost/ver-donaciones
@app.route("/ver-donaciones")
def donations():
    data=[]
    for donation in db.get_donations(page=1):
        donation_id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular = donation
        _, comuna_nom=db.get_comuna_nom(comuna_id)
        _, ruta_archivo, nombre_archivo, _= db.get_photo_by_donation_id(donation_id)
        img_filename= f"{ruta_archivo}/{nombre_archivo}"
        data.append({
            "comuna_nom": comuna_nom,
            "calle_numero": calle_numero,
            "tipo": tipo,
            "cantidad": cantidad,
            "fecha": fecha_disponibilidad,
            "descripcion": descripcion,
            "condiciones_retirar": condiciones_retirar,
            "nombre": nombre,
            "email": email,
            "celular": celular,
            "img_filename": img_filename,
        })

    return render_template("tables/ver-donaciones.html",data=data)

#http://localhost/ver-pedidos
@app.route("/ver-pedidos")
def requests():
    data=[]
    for request in db.get_requests(page=1):
        _, comuna_id, tipo, descripcion, cantidad, nombre, email, celular = request
        _, comuna_nom=db.get_comuna_nom(comuna_id)
        data.append({
            "comuna_nom": comuna_nom,
            "tipo": tipo,
            "descripcion": descripcion,
            "cantidad": cantidad,
            "nombre": nombre,
            "email": email,
            "celular": celular,
        })
        
    return render_template("tables/ver-pedidos.html",data=data)

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