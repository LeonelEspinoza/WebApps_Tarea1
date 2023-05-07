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
	cursor.execute("SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion ORDER BY id DESC LIMIT %s,%s;",((page-1)*5,page*5))
	donations = cursor.fetchall()
	return donations

def create_donation(a,b,c,d,e,f,g,h,i,j):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(a,b,c,d,e,f,g,h,i,j))
	conn.commit()

def get_donation_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion WHERE id=%s;", (id,))
	donation = cursor.fetchone()
	return donation

def get_requests(page):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido ORDER BY id DESC LIMIT %s,%s;",((page-1)*5,page*5))
	requests = cursor.fetchall()
	return requests


def create_request(a,b,c,d,e,f,g):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES (%s, %s, %s, %s, %s, %s, %s);",(a,b,c,d,e,f,g))
	conn.commit()

def get_request_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido WHERE id=%s;", (id,))
	request = cursor.fetchone()
	return request