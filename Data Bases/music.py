import sqlite3 as sq
from data import *

with sq.connect('saper.db') as con:
 cur = con.cursor()

with sq.connect('music.db') as con:
 con.execute('PRAGMA foreign_keys = ON')
 cur = con.cursor()
 cur.execute("""CREATE TABLE IF NOT EXISTS tracks(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    second INTEGER NOT NULL,
    price REAL NOT NULL,
    album_id INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE ON UPDATE CASCADE 
 )""")

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.executemany("INSERT INTO tracks VALUES (?, ?, ?, ?, ?)", info_tracks)

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.execute("""CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artist(id) ON DELETE CASCADE ON UPDATE CASCADE 
 )""")

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.executemany("INSERT INTO albums VALUES (?, ?, ?)", info_albums) 

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.execute("""CREATE TABLE IF NOT EXISTS artist(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
 )""")

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.executemany("INSERT INTO artist VALUES (?, ?)", info_artist) 

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.execute("SELECT tracks.title, second, price, albums.title FROM tracks INNER JOIN " "albums ON tracks.album_id = album_id")
 result = cur.fetchall()
print(result)

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.execute("SELECT tracks.title, second, albums.title, artist.name FROM tracks INNER JOIN " 
             "albums ON tracks.album_id = album_id LEFT JOIN "
             "artist ON albums.artist_id = artist.id")
 result = cur.fetchall()
print(result)

with sq.connect('music.db') as con:
 cur = con.cursor()
 cur.execute("SELECT tracks.title, second, price, albums.title FROM tracks INNER JOIN " "albums ON tracks.album_id = album_id WHERE artist_id = 2")
 result = cur.fetchall()
print(result)
