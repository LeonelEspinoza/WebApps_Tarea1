import pymysql
import json

DB_NAME = "tarea2"
DB_NAME = "confesiones"
DB_USERNAME = "dbadmin"
DB_PASSWORD = "dbadmin"
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