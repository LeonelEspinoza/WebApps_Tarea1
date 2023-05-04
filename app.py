from flask import Flask, render_template

app = Flask(__name__)

#http://localhost

#Rutas de nuestra app
#http://localhost/
@app.route("/")
def index():
    return render_template("inicio.html")

#http://localhost/login
@app.route("/login")
def login():
    pass