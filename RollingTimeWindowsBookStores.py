import yaml
import mysql.connector

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

db = yaml.safe_load(open("db.yaml"))

config = {
    'user': db['user'],
    'password': db['pwrd'],
    'host': db['host'],
    'database': 'MRTS',
    'auth_plugin': 'mysql_native_password'
}

book = "Book"
grocery = "Grocery"
store_name = book
cnx = mysql.connector.connect(**config)

store_sql= pd.read_sql_query(f"""
SELECT value, period
FROM mrts_table
WHERE Kind_of_Business = "{store_name} stores"
ORDER BY period;
""", cnx)

store = pd.DataFrame(store_sql, columns=["value", "period"])


plt.plot(store["period"], store["value"])
plt.gca().set(title=f"Monthly Sales of {store_name} Stores", xlabel = "Months", ylabel = "Sales")


ma4_store = store["value"].rolling(4).mean()

plt.figure()
plt.plot(store["period"], ma4_store, 'g')
plt.gca().set(title=f"Monthly Sales of {store_name} Stores with 4 month moving average", xlabel = "Months", ylabel = "Sales")


ma12_store = store["value"].rolling(12).mean()


plt.figure()
plt.plot(store["period"], ma12_store, 'k')
plt.gca().set(title=f"Monthly Sales of {store_name} Stores with 12 month moving average", xlabel = "Months", ylabel = "Sales")

plt.show()
