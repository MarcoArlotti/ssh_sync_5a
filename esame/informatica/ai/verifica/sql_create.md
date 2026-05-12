Certamente! Se ti stai preparando per una verifica su SQLite3 (o SQL in generale), devi padroneggiare la creazione di tabelle, i vincoli di integrità, le relazioni tra tabelle e le operazioni di manipolazione dati.

Ecco uno schema SQL completo e commentato che include tutti i concetti chiave solitamente richiesti.

---

## 1. Creazione delle Tabelle (DDL)

In questo esempio simuliamo un sistema di gestione per un **E-commerce**. Useremo i tipi di dato principali e i vincoli più comuni.

```sql
-- Abilitiamo il supporto alle chiavi esterne (fondamentale in SQLite)
PRAGMA foreign_keys = ON;

-- Tabella Categorie (Relazione 1 a N con Prodotti)
CREATE TABLE IF NOT EXISTS categorie (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    descrizione TEXT
);

-- Tabella Prodotti
CREATE TABLE IF NOT EXISTS prodotti (
    id_prodotto INTEGER PRIMARY KEY AUTOINCREMENT,
    codice_sku TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    prezzo REAL NOT NULL CHECK(prezzo >= 0), -- Vincolo di controllo
    scorta_magazzino INTEGER DEFAULT 0,
    id_categoria INTEGER,
    -- Definizione della Chiave Esterna
    FOREIGN KEY (id_categoria) REFERENCES categorie(id_categoria) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE
);

-- Tabella Clienti
CREATE TABLE IF NOT EXISTS clienti (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    data_iscrizione DATE DEFAULT CURRENT_DATE
);

-- Tabella Ordini (Tabella di associazione per relazione N a N)
CREATE TABLE IF NOT EXISTS ordini (
    id_ordine INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_prodotto INTEGER NOT NULL,
    quantita INTEGER NOT NULL CHECK(quantita > 0),
    data_ordine TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clienti(id_cliente),
    FOREIGN KEY (id_prodotto) REFERENCES prodotti(id_prodotto)
);

```

---

## 2. Concetti Chiave da Ricordare

In una verifica, assicurati di saper spiegare questi elementi presenti nello schema:

* **`PRIMARY KEY AUTOINCREMENT`**: Identifica univocamente ogni riga e aumenta automaticamente il valore.
* **`NOT NULL`**: Impedisce di lasciare il campo vuoto.
* **`UNIQUE`**: Impedisce duplicati (es. due email uguali).
* **`CHECK`**: Impone una condizione logica (es. il prezzo non può essere negativo).
* **`DEFAULT`**: Assegna un valore se non viene specificato (es. la data odierna).
* **`FOREIGN KEY`**: Crea il legame tra due tabelle per l'integrità referenziale.

---

## 3. Operazioni di Manipolazione (DML)

Ecco le query "classiche" che potrebbero chiederti di scrivere:

### Inserimento (INSERT)

```sql
INSERT INTO categorie (nome, descrizione) VALUES ('Elettronica', 'Gadget e dispositivi');
INSERT INTO prodotti (codice_sku, nome, prezzo, id_categoria) VALUES ('LAP-001', 'Laptop Pro', 1200.50, 1);

```

### Selezione con Filtri e Join (SELECT)

Questa è la parte più importante della verifica:

```sql
-- Visualizza i prodotti con il nome della loro categoria
SELECT p.nome, p.prezzo, c.nome AS categoria
FROM prodotti p
JOIN categorie c ON p.id_categoria = c.id_categoria
WHERE p.prezzo > 500
ORDER BY p.prezzo DESC;

```

### Aggregazione (GROUP BY)

```sql
-- Conta quanti prodotti ci sono per ogni categoria
SELECT c.nome, COUNT(p.id_prodotto) AS totale_prodotti
FROM categorie c
LEFT JOIN prodotti p ON c.id_categoria = p.id_categoria
GROUP BY c.nome;

```

### Aggiornamento e Cancellazione (UPDATE/DELETE)

```sql
-- Aggiorna il prezzo di un prodotto specifico
UPDATE prodotti SET prezzo = 1100.00 WHERE codice_sku = 'LAP-001';

-- Elimina un cliente che non ha effettuato ordini
DELETE FROM clienti WHERE id_cliente NOT IN (SELECT id_cliente FROM ordini);

```

---

## 4. Modifica della Struttura (ALTER TABLE)

Se il prof chiede come aggiungere una colonna a test già iniziato:

```sql
ALTER TABLE clienti ADD COLUMN telefono TEXT;

```

### Piccolo suggerimento per la lode:

Se ti chiedono la differenza tra `JOIN` e `LEFT JOIN`:

* **`JOIN`**: Restituisce solo le righe che hanno una corrispondenza in entrambe le tabelle.
* **`LEFT JOIN`**: Restituisce tutte le righe della tabella di sinistra, anche se non c'è una corrispondenza in quella di destra (utile per vedere categorie "vuote").