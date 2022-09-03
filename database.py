import sqlite3

connection = sqlite3.connect('scores.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Scores (Score INT)''')

connection.commit()
connection.close()