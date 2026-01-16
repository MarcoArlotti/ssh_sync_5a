import sqlite3
import os

# Definiamo dove creare il file del database (nella cartella instance)
if not os.path.exists('arlotti_14\instance'):
    os.makedirs('arlotti_14\instance')

db_path = os.path.join('arlotti_14\instance', 'video.db')

# Ci connettiamo (se il file non esiste, lo crea)
connection = sqlite3.connect(db_path)

# Leggiamo lo schema SQL
with open('arlotti_14\\app\\yotube.sql') as f:
    connection.executescript(f.read())

print("Database creato con successo in:", db_path)
connection.close()