# Fondamenti di Python e Gestione Progetto

## Python: Tipizzazione dinamica vs statica e Type Hints
Python è un linguaggio **a tipizzazione dinamica**, il che significa che non è necessario dichiarare il tipo di una variabile esplicitamente; il tipo viene determinato a runtime. Ad esempio:

```python
x = 10      # Python capisce che è un int
x = "ciao"  # ora x è str
```

La tipizzazione dinamica offre **flessibilità** e **rapidità di sviluppo**, ma può generare errori non evidenti fino all'esecuzione.

I **Type Hints**, introdotti con PEP 484, permettono di specificare i tipi delle variabili e delle funzioni, migliorando leggibilità e strumenti di analisi statica (es. MyPy):

```python
def somma(a: int, b: int) -> int:
    return a + b
```

I Type Hints **non cambiano il comportamento a runtime**, ma aiutano a prevenire errori e documentano il codice.

---

## Ambiente di lavoro: `venv` e `requirements.txt`

* **`venv`**: permette di creare ambienti isolati per progetto, evitando conflitti tra dipendenze di progetti diversi.

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

* **`requirements.txt`**: elenca le dipendenze del progetto. Utile per replicare l'ambiente:

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

L'isolamento assicura che aggiornamenti di librerie in un progetto non rompano altri progetti.

---

## Versionamento: `.gitignore` e sicurezza

* **`.gitignore`** serve a escludere file dal controllo versione, come ambienti virtuali, file di configurazione locali o credenziali:

```
env/
*.pyc
instance/
.env
```

* Non inserire mai file sensibili (password, SECRET_KEY) su GitHub. Usare variabili d'ambiente o file `.env` esclusi dal repo.

---

## Variabili d'Ambiente: `.env` e protezione della SECRET_KEY

Le variabili d'ambiente permettono di separare configurazioni sensibili dal codice. Ad esempio, con **python-dotenv**:

```python
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
```

Il file `.env` non va mai committato. Questo protegge la **SECRET_KEY** e altre credenziali.

---

# Progettazione Database (Modello ER e Vincoli)

## Modello ER: Componenti e cardinalità

* **Entità**: oggetti del dominio (es. `Utente`, `Prodotto`)
* **Attributi**: proprietà delle entità (es. `nome`, `email`)
* **Relazioni**: collegano entità tra loro (es. `Acquista`)

**Cardinalità**:

* 1:1 → un record di A corrisponde a uno di B
* 1:N → un record di A corrisponde a molti di B
* N:N → molti record di A corrispondono a molti di B (richiede tabella di raccordo)

---

## Logica Relazionale: tabella di raccordo

Per relazioni molti-a-molti si crea una **tabella di raccordo**:

```
Utente(id_utente, nome)
Corso(id_corso, titolo)
Utente_Corso(id_utente, id_corso)
```

---

## Integrità e Qualità

* **Chiave Primaria (PK)**: identifica univocamente un record
* **Chiave Esterna (FK)**: collega tabelle garantendo integrità referenziale
* **Vincoli**:

  * `UNIQUE`: valori univoci
  * `NOT NULL`: obbligatorio
  * `CHECK`: verifica condizioni specifiche

---

## Design-First

Analizzare requisiti e creare **diagrammi ER prima di scrivere codice** evita ridondanze, errori e facilita manutenzione.

---

# Normalizzazione, DBMS e Transazioni (ACID)

## Normalizzazione

* **1NF**: rimuove dati ripetuti in colonne separate
* **2NF**: rimuove dipendenze parziali su PK composite
* **3NF**: rimuove dipendenze transitiva tra attributi non chiave

Risolve anomalie di **inserimento, aggiornamento e cancellazione**.

---

## DBMS

* **DB**: collezione di dati
* **DBMS**: software che gestisce accesso, sicurezza e concorrenza dei dati

Controllo concorrenza evita conflitti quando più utenti modificano dati contemporaneamente.

---

## Proprietà ACID

* **Atomicità**: operazione completa o nulla
* **Consistenza**: dati validi
* **Isolamento**: transazioni non interferiscono
* **Durabilità**: modifiche permanenti anche in caso di crash

---

## NoSQL

* Modelli non relazionali: documenti, key-value, colonne larghe
* Utile per **Big Data** o dati non strutturati
* Scambio tra flessibilità e rigidità del modello relazionale

---

# Linguaggio SQL e Integrazione con Flask

## Comandi SQL

* **DDL**: definizione struttura (`CREATE TABLE`, `ALTER TABLE`)
* **DML**: gestione dati (`INSERT`, `UPDATE`, `DELETE`)

**Query avanzate**:

```sql
SELECT categoria, COUNT(*) 
FROM prodotti 
GROUP BY categoria 
HAVING COUNT(*) > 5;
```

**JOIN**:

* **INNER JOIN**: solo record corrispondenti
* **LEFT JOIN**: tutti da sinistra, null se mancanti a destra

---

## Sicurezza DB

* Protezione da **SQL Injection** con query parametrizzate
* Evitare concatenazioni di stringhe con input utente

---

## Flask & DB

* **SQLite** semplice per sviluppo
* File `.sqlite` nella cartella `instance/`, non versionato
* Separare configurazione da codice

---

## Pattern Architetturali

* Separare query dalle route aumenta manutenibilità e testabilità
* Ad esempio: usare layer `models.py` o repository pattern

---

# Architettura Web con Flask e Jinja2

## Struttura App

* **`__init__.py`**: inizializza app, registra blueprint
* **Blueprints**: organizzazione modulare per progetti grandi

---

## Frontend Dinamico

* **Jinja2**: template engine per HTML dinamico
* **Ereditarietà**: `{% extends "base.html" %}` evita duplicazioni

---

## Ciclo Request/Response

* Client invia **request** → server elabora → invia **response**
* Status code: 200 OK, 404 Not Found, 500 Internal Server Error
* **GET**: leggere dati, **POST**: inviare dati

---

## Protocollo HTTP

* Stateless per design
* **Sessioni** mantengono stato dell’utente lato server tramite cookie

---

# API, Sicurezza e Deployment

## Concetto di API

* Analogia: **ristorante** → client (cliente) chiede piatto (risorsa), server (cucina) risponde
* Stile REST: risorse, URL significativi, metodi HTTP coerenti

---

## Endpoint

* Struttura: `URL + Metodo`

```python
@app.route("/utente/<id>", methods=["GET"])
def get_utente(id):
    ...
```

---

## Sicurezza Utenti

* **Autenticazione**: verificare identità
* **Autorizzazione**: controllare permessi
* Hashing password con `generate_password_hash`
* Audit: traccia azioni utenti critiche

---

## Messa in produzione

* Ambiente **Sviluppo**: debug, errori visibili
* Ambiente **Produzione**: ottimizzato, stabile
* **Gunicorn**: server WSGI per gestire Flask in produzione
* Piattaforme come Render hanno filesystem effimero → usare DB esterni o storage persistente
