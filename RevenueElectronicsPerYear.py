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
    SUM(value) AS revenue
FROM mrts_table
WHERE Kind_of_Business = 'Electronics stores'
GROUP BY 1
HAVING SUM(value) > 0;
""")
try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        cursor = cnx.cursor()

        cursor.execute(sql)
        
        year = []
        revenue = []
        
        for row in cursor.fetchall():
            print(row)
            year.append(row[0])
            revenue.append(row[1])
            
        cursor.close()
        cnx.close()
        
except Error as e:
    print("Error occured while connecting to MySQL", e)

plt.plot(year, revenue)
plt.xlabel("Year")
plt.ylabel("Revenue in $")
plt.title("Total revenue from Electronics stores per year")
plt.show()


