import sqlite3

connection = sqlite3.connect('business.db')

connection.execute('DELETE FROM products')                 # Delete all rows in products
connection.commit()