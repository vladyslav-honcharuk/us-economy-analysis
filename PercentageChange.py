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

sql_men = pd.read_sql_query("""
SELECT period, value
FROM mrts_table
WHERE Kind_of_Business in (
    "Men's clothing stores")
ORDER BY period;
""", cnx)

sql_woman = pd.read_sql_query("""
SELECT period, value
FROM mrts_table
WHERE Kind_of_Business in (
    "Women's clothing stores")
ORDER BY period;
""", cnx)

sql_clothing = pd.read_sql_query("""
SELECT period, value
FROM mrts_table
WHERE Kind_of_Business in (
    "Clothing stores")
ORDER BY period;
""", cnx)

men = pd.DataFrame(sql_men, columns=['period', 'value'])[:-12]

woman = pd.DataFrame(sql_woman, columns=['period', 'value'])[:-12]

whole = pd.DataFrame(sql_clothing, columns=['period', 'value'])[:-12]

men_pct = men["value"].pct_change()
woman_pct = woman["value"].pct_change()

men_pct_whole = np.divide(men["value"], whole["value"])
woman_pct_whole = np.divide(woman["value"], whole["value"])

plt.plot(men["period"], men_pct, label="Men's")
plt.plot(woman["period"], woman_pct, label="Woman's")
plt.legend()
plt.gca().set(title="Monthly Percentage Change of Clothing Stores Sales", xlabel = "Months", ylabel = "Percent of change")

plt.figure()
plt.plot(men["period"], men_pct_whole, label="Men's")
plt.plot(woman["period"], woman_pct_whole, label="Woman's")
plt.legend()
plt.gca().set(title="Monthly Sales of Woman and Men Clothing as a percent of whole Sales", xlabel = "Months", ylabel = "Percent of change")
plt.show()

