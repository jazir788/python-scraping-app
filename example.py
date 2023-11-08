import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM 'event' WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT band,date FROM 'event' WHERE date='2088.10.14'")
rows = cursor.fetchall()
print(rows)

#Insert new rows
#new_rows = [('Hens', 'Hens City', '2088.10.17'),
#            ('Cats','Cats City', '2088.10.17')
#            ]
#
#cursor.executemany("INSERT INTO event VALUES(?,?,?)", new_rows)
#connection.commit()


cursor.execute("SELECT * FROM 'event'")
rows = cursor.fetchall()
print(rows)