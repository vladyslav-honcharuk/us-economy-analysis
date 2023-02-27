import yaml
import mysql.connector
from mysql.connector import Error

#connect to the MySQL Server with yaml
db = yaml.safe_load(open("db.yaml"))

config = {
    'user': db['user'],
    'password': db['pwrd'],
    'host': db['host'],
    'database': 'MRTS',
    'auth_plugin': 'mysql_native_password'
}

# Create the database
try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS MRTS")
        print("MRTS database is created")
except Error as e:
    print("Error occured while connecting to MySQL", e)

    