import sqlite3

connection = sqlite3.connect('business.db')

connection.execute('UPDATE products SET weight = ?', [9])  # Set all weights to 9
connection.commit()