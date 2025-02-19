import sqlite3

connection = sqlite3.connect('database.db')

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password, reserve) VALUES (?, ?, ?)",
            ('admin', '0000', 1000)
            )

connection.commit()
connection.close()