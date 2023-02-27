import pandas as pd
import numpy as np

import yaml
import mysql.connector
import matplotlib.pyplot as plt

db = yaml.safe_load(open("db.yaml"))

config = {
    'user': db['user'],
    'password': db['pwrd'],
    'host': db['host'],
    'database': 'MRTS',
    'auth_plugin': 'mysql_native_password'
}

cnx = mysql.connector.connect(**config)
if cnx.is_connected():
    cursor = cnx.cursor()


def RFS_trend():
    """Draws trends of total retail and food services sales"""

    sql = ("""
    SELECT period, value
    FROM mrts_table
    WHERE Kind_of_business = 'Retail and food services sales, total'
    ORDER BY period;
    """)

    sql_year = ("""
    SELECT YEAR(period) as year, SUM(value) as total
    FROM mrts_table
    WHERE Kind_of_business = 'Retail and food services sales, total'
    GROUP BY 1
    ORDER BY year;
    """)
    cursor.execute(sql)

    period = []
    value = []

    for row in cursor.fetchall():
        period.append(row[0])
        value.append(row[1])

    plt.plot(period, value)
    plt.gca().set(title="Monthly Retail and Food Services", xlabel = "Months", ylabel = "Sales")

    cursor.execute(sql_year)

    period = []
    value = []

    for row in cursor.fetchall():
        period.append(row[0])
        value.append(row[1])

    plt.figure()
    plt.plot(period, value)
    plt.gca().set(title="Yearly Retail and Food Services", xlabel = "Years", ylabel = "Sales")

    plt.show()

#RFS_trend()

def Comparing():
    """Comparison of bookstores, sporting goods stores, and hobbies, toys, and games stores trends"""

    sql_query = pd.read_sql_query("""
    SELECT Kind_of_Business, period, value
    FROM mrts_table
    WHERE Kind_of_Business in ('Book stores',
    'Sporting goods stores', 'Hobby, toy, and game stores')
    ORDER BY period;
    """, con=cnx)

    sql_query_year = pd.read_sql_query("""
    SELECT Kind_of_Business, YEAR(period) as year, SUM(value) as total
    FROM mrts_table
    WHERE Kind_of_Business in ('Book stores',
    'Sporting goods stores', 'Hobby, toy, and game stores')
    GROUP BY 1, 2
    ORDER BY period;    
    """, con=cnx)

    df = pd.DataFrame(sql_query, columns=['Kind_of_Business', 'period', 'value'])

    df_sport = df[df["Kind_of_Business"] == "Sporting goods stores"]
    df_htg = df[df["Kind_of_Business"] == "Hobby, toy, and game stores"]
    df_book = df[df["Kind_of_Business"] == "Book stores"]

    plt.figure()
    plt.plot(df_sport["period"], df_sport["value"], label="Sporting goods stores")
    plt.plot(df_htg["period"], df_htg["value"], label="Hobby, toy, and game stores")
    plt.plot(df_book["period"], df_book["value"], label="Book stores")


    plt.gca().set(title="Monthly sales", xlabel = "Months", ylabel = "Sales")
    plt.legend()

    df_year = pd.DataFrame(sql_query_year, columns=['Kind_of_Business', 'year', 'total'])
    df_sport = df_year[df_year["Kind_of_Business"] == "Sporting goods stores"]
    df_htg = df_year[df_year["Kind_of_Business"] == "Hobby, toy, and game stores"]
    df_book = df_year[df_year["Kind_of_Business"] == "Book stores"]

    plt.figure()
    plt.plot(df_sport["year"], df_sport["total"], label="Sporting goods stores")
    plt.plot(df_htg["year"], df_htg["total"], label="Hobby, toy, and game stores")
    plt.plot(df_book["year"], df_book["total"], label="Book stores")


    plt.gca().set(title="Yearly sales", xlabel = "Years", ylabel = "Sales")
    plt.legend()

    plt.show()
  
Comparing()

cursor.close()
cnx.close()

    