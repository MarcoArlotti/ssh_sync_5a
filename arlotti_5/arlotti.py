import sqlite3


# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('fabio.db')
# 3. Creazione Cursoredb
cursor = conn.cursor()

def create_tables():
    try:
        #AUTORI
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Autori (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                titolo TEXT NOT NULL
            )
        """)
        #LIBRI
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Libri (
                id INTEGER PRIMARY KEY,
                titolo TEXT NOT NULL,
                autore_id INTEGER NOT NULL,
                anno INTEGER,
                genere TEXT NOT NULL,
                FOREIGN KEY (autore_id) REFERENCES Autori(id)
            )
        """)
        #PRESTITI
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prestiti (
                id INTEGER PRIMARY KEY,
                libro_id INTEGER,
                utente TEXT NOT NULL,
                data_prestito TEXT,
                data_restituzione TEXT,
                FOREIGN KEY (libro_id) REFERENCES Libri(id)
            )
        """)

    finally:
        # 6. Chiusura Connessione
        conn.close()

def insert_data():

    autori = [
        (1,'Mario','Rossi'),
        (2,'Lucia','Bianchi'),
        (3,'Alessandro','Verdi')
        ]

    libri = [
        (1,'Il mistero del castello', 1, 2020, 'Giallo'),
        (2,'Viaggio nel tempo', 1, 2018, 'Fantascienza'),
        (3,'La cucina italiana', 2, 2019, 'Cucina'),
        (4,'Storia antica', 3, 2021, 'Storia'),
        (5,'Romanzo moderno', 3, 2022, 'Narrativa'),
        (6,'Il ritorno del castello', 1, 2023, 'Giallo')
        ]

    prestiti = [
        (1, 1, 'Mario Rossi', '2023-01-01', '2023-01-15'),
        (2, 2, 'Lucia Bianchi', '2023-02-01', None),
        (3, 3, 'Alessandro Verdi', '2023-03-01', '2023-03-10'),
        (4, 4, 'Mario Rossi', '2023-04-01', None)
    ]
    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    cursor.executemany("INSERT OR REPLACE INTO Autori (id,nome,titolo) VALUES (?,?,?)", autori)
    cursor.executemany("INSERT OR REPLACE INTO Libri (id,titolo,autore_id,anno,genere) VALUES (?,?,?,?,?)", libri)
    cursor.executemany("INSERT OR REPLACE INTO Prestiti (id,libro_id,utente,data_prestito,data_restituzione) VALUES (?,?,?,?,?)", prestiti)
    
    conn.commit()

insert_data()
create_tables()
# Elenco di tutti i libri con titolo,
# anno e nome dell'autore (usa JOIN).
def uno():
    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Libri.titolo, Libri.anno, Autori.nome, Autori.titolo
        FROM Libri
        JOIN Autori ON Libri.autore_id = Autori.id;
    """
    )
    autore_ris = cursor.fetchall()
    for i in autore_ris:
        print(f"titolo: {i[0]}, anno: {i[1]} nome autore: {i[2]} {i[3]}")
    conn.close()

def due():
    # Elenco di tutti i prestiti con titolo del libro,
    # utente e data di prestito (usa JOIN). Risultato
    
    # 2. Connessione: crea il file 'scuola.db' se non esiste

    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Libri.titolo, Prestiti.utente, Prestiti.data_prestito
        FROM Prestiti
        JOIN Libri ON Libri.libri_id = Libri.id
        JOIN Autori ON Libri.autori_id = Autori.id;
    """
    )
    autore_ris = cursor.fetchall()
    for i in autore_ris:
        print(f"")
    conn.close()

# uno()
due()