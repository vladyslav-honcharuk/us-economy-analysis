import yaml
import mysql.connector
from mysql.connector import Error

db = yaml.safe_load(open("db.yaml"))

config = {
    'user': db['user'],
    'password': db['pwrd'],
    'host': db['host'],
    'database': 'MRTS',
    'auth_plugin': 'mysql_native_password'
}

try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM MRTS_table")
        
        i = 0
        for row in cursor.fetchall():
            if i < 20:
                print(row)
                i+=1
            
        cursor.close()
        cnx.close()
        
except Error as e:
    print("Error occured while connecting to MySQL", e)

    