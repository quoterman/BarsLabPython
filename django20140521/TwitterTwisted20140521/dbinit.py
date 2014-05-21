import sqlite3

conn = sqlite3.connect("db.db")

cursor = conn.cursor()

cursor.execute("create table tweets (tweet varchar(140))")
conn.commit()
conn.close()