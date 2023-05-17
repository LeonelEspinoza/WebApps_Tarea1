import re
import filetype

def validate_exist(value):
    return value!=None

def validate__name(value):
    return value and len(value)<81 and len(value)>2

def validate_email(value):
    valid=re.match(r"[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*",str(value))
    if valid:
        return True
    return False

def validate_phone(value):
    if(value==None):
       return True
    valid=re.match(r"\+569[0-9]{8}",str(value))
    if valid:
        return True
    return False

def validate_fileType(value):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    if validate_exist(value)==False:
        return False
    
    if value.filename== "":
        return False

    ftype_guess =filetype.guess(value)

    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False

    return True

def validate_donation(region,comuna,calle_numero,tipo_donacion,cantidad,
                      fecha,foto_donacion,
                      nombre,email,celular):
    invalid=[]
    if (validate_exist(region)!=True):
       invalid.append("Falta region")

    if (validate_exist(comuna)!=True):
       invalid.append("Falta comuna")

    if (validate_exist(calle_numero)!=True):
       invalid.append("Falta numero de calle")

    if (validate_exist(tipo_donacion)!=True):
       invalid.append("Falta tipo de donación")

    if (validate_exist(cantidad)!=True):
       invalid.append("Falta cantidad")

    if (validate_exist(fecha)!=True):
       invalid.append("Falta fecha")
    
    if(validate_fileType(foto_donacion)!=True):
       invalid.append("Archivo invalido")

    if (validate__name(nombre)!=True):
       invalid.append("Nombre invalido")

    if (validate_email(email)!=True):
       invalid.append("Email invalido")

    if (validate_phone(celular)!=True):
       invalid.append("Número celular invalido")
    return invalid

def validate_request(region, comuna, tipo_pedido, cantidad, descripcion, nombre, email, celular):
    invalid=[]
    if (validate_exist(region)!=True):
       invalid.append("Falta region")

    if (validate_exist(comuna)!=True):
       invalid.append("Falta comuna")

    if (validate_exist(tipo_pedido)!=True):
       invalid.append("Falta tipo de pedido")

    if (validate_exist(cantidad)!=True):
       invalid.append("Falta cantidad")

    if (validate_exist(descripcion)!=True):
       invalid.append("Falta descripcion")

    if (validate__name(nombre)!=True):
       invalid.append("Nombre invalido")

    if (validate_email(email)!=True):
       invalid.append("Email invalido")

    if (validate_phone(celular)!=True):
       invalid.append("Número celular invalido")
    return invalid