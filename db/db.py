import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "root"
DB_PASSWORD = "liaes.160729"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"



# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

def get_donations(page):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion ORDER BY id DESC LIMIT %s,%s;",((page-1)*5,5))
	donations = cursor.fetchall()
	return donations

def create_donation(comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular))
	conn.commit()

def get_donation_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion WHERE id=%s;", (id,))
	donation = cursor.fetchone()
	return donation

def get_donation_id_by_values(comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM donacion WHERE comuna_id= %s AND calle_numero= %s AND tipo= %s AND cantidad= %s AND fecha_disponibilidad= %s AND descripcion= %s AND condiciones_retirar= %s AND nombre= %s AND email= %s AND celular= %s;", (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular))
	donation = cursor.fetchone()
	return donation

def get_requests(page):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido ORDER BY id DESC LIMIT %s,%s;",((page-1)*5,5))
	requests = cursor.fetchall()
	return requests


def create_request(comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES (%s, %s, %s, %s, %s, %s, %s);",(comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante))
	conn.commit()

def get_request_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido WHERE id=%s;", (id,))
	request = cursor.fetchone()
	return request

def insert_photo(path,filename,donation_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES (%s, %s, %s);", (path, filename, donation_id, ))
	conn.commit()

def get_photo_by_donation_id(donation_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, ruta_archivo, nombre_archivo, donacion_id FROM foto WHERE donacion_id=%s;", (donation_id, ))
	request = cursor.fetchone()
	return request

def get_photo_by_id(photo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, ruta_archivo, nombre_archivo, donacion_id FROM foto WHERE id=%s;", (photo_id, ))
	request = cursor.fetchone()
	return request

def get_comuna_id(region_id, nom_comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM comuna WHERE region_id=%s AND nombre= %s;", (region_id, nom_comuna))
	request = cursor.fetchone()
	return request