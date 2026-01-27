import sqlite3
import os

# Definiamo dove creare il file del database (nella cartella instance)
if not os.path.exists('blog_scolastico/instance'):
    os.makedirs('blog_scolastico/instance')

db_path = os.path.join('blog_scolastico/instance', 'blog.sqlite')

# Ci connettiamo (se il file non esiste, lo crea)
connection = sqlite3.connect(db_path)

# Leggiamo lo schema SQL
with open('blog_scolastico/app/schema.sql') as f:
    connection.executescript(f.read())

print("Database creato con successo in:", db_path)
connection.close()