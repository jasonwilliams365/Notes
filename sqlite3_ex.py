import sqlite3
conn = sqlite3.connect("example.db")
cur = conn.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)")

cur.execute("INSERT INTO people (name) VALUES (?)", ("Alice",))
conn.commit()
for row in cur.execute("SELECT * FROM people"):
    print(row)


conn.close()