import sqlite3

connection = sqlite3.connect('scores.db')

cursor = connection.cursor()

cursor.execute('''DELETE FROM Scores''')

cursor.execute('''SELECT * FROM Scores''')

print(cursor.fetchall())

# num=(4,)
# cursor.execute('INSERT INTO Scores VALUES (?)', num)

# cursor.execute('SELECT MAX(Score) FROM Scores')
#
# result = cursor.fetchall()
# print(result[0][0])

connection.commit()
connection.close()