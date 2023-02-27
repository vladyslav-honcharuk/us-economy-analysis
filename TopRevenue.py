import yaml
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt

db = yaml.safe_load(open("db.yaml"))

config = {
    'user': db['user'],
    'password': db['pwrd'],
    'host': db['host'],
    'database': 'MRTS',
    'auth_plugin': 'mysql_native_password'
}

sql = ("""
SELECT 
		YEAR(period), 
		SUM(value) AS revenue,
		Kind_of_Business
FROM mrts_table
GROUP BY 1, 3
HAVING SUM(value) > 0
ORDER BY revenue DESC;
""")
try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        cursor = cnx.cursor()

        cursor.execute(sql)
        
        for row in cursor.fetchall():
                print(row)

        cursor.close()
        cnx.close()
        
except Error as e:
    print("Error occured while connecting to MySQL", e)

