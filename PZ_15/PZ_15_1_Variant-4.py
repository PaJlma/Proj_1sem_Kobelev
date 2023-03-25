import sqlite3 as sq

with sq.connect('fakultet.bd') as con:
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS fakultet (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR)""")

with sq.connect('kafedra.db') as con:
   cur = con.cursor()
   cur.execute("""CREATE TABLE IF NOT EXISTS kafedra(
     id INTEGER PRIMARY KEY,
     name VARCHAR,
     id_fakultet INTEGER,
     FOREIGN KEY (id_fakultet) REFERENCES fakultet(id))""")

with sq.connect('specialties.bd') as con:
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS fakultet (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, FOREIGN KEY (kafedra_id) REFERENCES kafedra(id))""")