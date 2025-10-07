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

try:
    # Eseguo DDL per creare la tabella se non esiste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Corsi (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Matricola INTEGER NOT NULL,
            Corso TEXT NOT NULL,
            Voto INTEGER,
            FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
        )
    """)

    # 4. Esecuzione Query DML (parametrizzata)
    # Il segnaposto per SQLite è '?'
    cursor.executemany("INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)", lista_studenti)
    cursor.executemany("INSERT INTO Corsi (Matricola, Corso, Voto) VALUES (?, ?, ?)", corsi)

    # 5. Conferma delle modifiche
    conn.commit()
    #1
    cursor.execute("SELECT Matricola, Nome, Cognome FROM Studenti")
    studenti = cursor.fetchall() # I risultati sono tuple

    for studente in studenti:
        print(f"studente: {studente[0]}, Nome: {studente[1]}, Cognome: {studente[2]}")
    
    #2
    cursor.execute(
    """
    SELECT 
        Studenti.Nome, 
        Studenti.Cognome, 
        Corsi.Corso, 
        Corsi.Voto 
    FROM Studenti 
    JOIN Corsi ON Studenti.Matricola = Corsi.Matricola 
    WHERE Studenti.Matricola = ?
    """,
    (101,)
)
    studente = cursor.fetchone() # I risultati sono tuple
    if studente:
        print(f"Studente con matricola 101 (SQLite): {studente} {studente}")

    #3
    cursor.execute(
    """
    SELECT COUNT(*) FROM Corsi GROUP BY Matricola
    """
    )
    corso = cursor.fetchone() # I risultati sono tuple
    if corso:
        print(f"numero degli esami{corso}")




finally:
    # 6. Chiusura Connessione
    conn.close()

    