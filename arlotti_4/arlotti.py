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


#Restituisce tutti i libri di un autore specifico (usa JOIN).
def query_libri_per_autore(autore_id):
    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Autori.id, Libri.id, Libri.titolo
        FROM Libri
        JOIN Autori ON Libri.autore_id = Autori.id
        where Autori.id = ?
    """,
    (autore_id,)
    )
    autore_ris = cursor.fetchall()
    for i in autore_ris:
        print(f"Autore: {i[0]}, Libro ID: {i[1]}, Titolo: {i[2]}")
    conn.close()

def query_prestiti_per_utente(utente):
    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Prestiti.utente, Prestiti.data_prestito, Libri.titolo, Autori.nome
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
        JOIN Autori ON Libri.autore_id = Autori.id
        WHERE Prestiti.utente = ?;
    """,
    (utente,)
    )
    autore_ris = cursor.fetchall()
    for i in autore_ris:
        print(f"Utente: {i[0]}, Data prestito {i[1]}, Titolo: {i[2]}, Autore: {i[3]}")
    conn.close()

def query_libri_per_genere():
    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    """
    Restituisce il numero di libri 
    per genere (usa GROUP BY).
    Assicurati di avere almeno un genere
    con due libri nell'esempio (per esempio
    "Giallo" con 2 libri) in modo che la query
    mostri valori maggiori di 1.
    """

    cursor.execute("""
        SELECT genere, count(*) as NUMERO_LIBRI
        From Libri
        GROUP BY genere
    """,
    )
    autore_ris = cursor.fetchall()
    for i in autore_ris:
        print(f"Genere: {i[0]}, con {i[1]} libri")
    conn.close()

def query_autori_con_piu_libri():
    # Restituisce gli autori ordinati per numero di libri
    # (usa JOIN, GROUP BY, ORDER BY).

    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn = sqlite3.connect('fabio.db')
    # 3. Creazione Cursore
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Libri.autore_id, count(*) AS TOT
        GROUP BY Libri.autore_id
        ORDER BY TOT
    """,
    )
    autore_ris = cursor.fetchall()
    for i in autore_ris:
        print(f"Genere: {i[0]}, con {i[1]} libri")
    conn.close()

def query_prestiti_non_restituiti():
    pass

create_tables()
insert_data()
# query_libri_per_autore(autore_id=3)
# query_prestiti_per_utente(utente='Alessandro Verdi')
# query_libri_per_genere()
query_autori_con_piu_libri()