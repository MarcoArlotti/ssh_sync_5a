import sqlite3
    
lista_studenti = [
    (101, 'Mario', 'Rossi'),
    (102, 'Lucia', 'Bianchi'),
]
corsi = [
    (101, "Matematica", 28),
    (102, "Informatica", 30),
    (103, "Fisica", 27),
]
# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('scuola.db')
# 3. Creazione Cursore
cursor = conn.cursor()

def create_tables():
    try:
        # Eseguo DDL per creare la tabella se non esiste
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Studenti (
                Matricola INTEGER PRIMARY KEY,
                Nome TEXT NOT NULL,
                Cognome TEXT NOT NULL"""
            )
    finally:
        # 6. Chiusura Connessione
        conn.close()

def insert_data():
    