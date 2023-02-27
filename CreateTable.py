import yaml
import mysql.connector
from mysql.connector import Error
import csv

db = yaml.safe_load(open("db.yaml"))

config = {
    'user': db['user'],
    'password': db['pwrd'],
    'host': db['host'],
    'database': 'MRTS',
    'auth_plugin': 'mysql_native_password'
}
# Execute the database
try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        cursor = cnx.cursor()
        cursor.execute("SELECT database();")
        record = cursor.fetchone()
        print("Connected to: ", record)
        
        print("Creating table:")
        cursor.execute("DROP TABLE IF EXISTS MRTS_table")
        cursor.execute("""CREATE TABLE `MRTS_table` (`ID` INT NOT NULL, `Kind_of_Business` VARCHAR(100) NOT NULL,
                       `period` DATE NOT NULL, `value` FLOAT(10, 2) NOT NULL, PRIMARY KEY (`ID`))""")
        print("Table is created")

        with open('mrts.csv') as file:
            #read csv file
            mrts_database=csv.reader(file, delimiter=',')
            next(mrts_database)
            #loop through data
            for row in mrts_database:
                sql = "INSERT INTO MRTS.MRTS_table VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, row)
                cnx.commit()
            print("Table is filled with data")
        
        cursor.close()
        cnx.close()
        
except Error as e:
    print("Error occured while connecting to MySQL", e)

    