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
Le tre forme di normalizzazione non si applicano direttamente al diagramma **ER (Entity-Relationship)**, ma al **modello relazionale** (cioè alle tabelle e ai database logici) che si ottiene traducendo quel diagramma ER.

La normalizzazione è un processo di ottimizzazione. Il suo scopo principale è **eliminare la ridondanza dei dati** e **prevenire le anomalie** di inserimento, modifica e cancellazione.

Ecco a cosa servono e cosa fanno, passo dopo passo, le prime tre forme normali (1NF, 2NF, 3NF):

---

### 1. Prima Forma Normale (1NF): *Garantire l'atomicità*

Serve a fare in modo che ogni cella di una tabella contenga un solo valore e che non ci siano gruppi di dati ripetuti.

* **Cosa elimina:** Campi multimvalore (es. una cella "Telefono" con dentro tre numeri diversi) o tabelle nidificate.
* **Regola:** Tutti gli attributi devono essere **atomici** (non ulteriormente scomponibili) e deve essere definita una chiave primaria.

### 2. Seconda Forma Normale (2NF): *Eliminare la dipendenza parziale*

Si applica solo alle tabelle che hanno una **chiave primaria composta** (fatta da più colonne). Serve a garantire che ogni dato nella tabella dipenda dall'intera chiave e non solo da un pezzo di essa.

* **Cosa elimina:** La ridondanza causata da dati che si riferiscono solo a una parte della chiave.
* **Regola:** La tabella deve essere in 1NF e tutti gli attributi non-chiave devono dipendere interamente dall'intera chiave primaria.
* *Esempio:* Se hai una tabella `Dettaglio_Ordine` con chiave (`IdOrdine`, `IdProdotto`), il campo `PrezzoProdotto` dipende solo da `IdProdotto`, non dall'ordine. Va quindi spostato in una tabella separata `Prodotti`.

### 3. Terza Forma Normale (3NF): *Eliminare la dipendenza transitiva*

Serve a fare in modo che i dati non-chiave dipendano *solo* dalla chiave primaria, e non da altri campi non-chiave.

* **Cosa elimina:** L'effetto "catena" o dipendenza indiretta.
* **Regola:** La tabella deve essere in 2NF e nessun attributo non-chiave deve dipendere da un altro attributo non-chiave.
* *Esempio:* Se in una tabella `Impiegati` hai `IdImpiegato` (chiave), `IdDipartimento` e `NomeDipartimento`, il `NomeDipartimento` dipende dall'ID del dipartimento, non direttamente dall'impiegato. Per essere in 3NF, i dati del dipartimento vanno isolati in una tabella `Dipartimenti`.

---

### In sintesi: perché sono fondamentali?

Se non si normalizza il database derivato dall'ER, si va incontro a tre grossi problemi:

1. **Anomalie di Inserimento:** Non puoi inserire un dato se non ne conosci un altro (es. non puoi registrare un nuovo dipartimento se non gli assegni almeno un impiegato).
2. **Anomalie di Cancellazione:** Se cancelli un record, rischi di perdere informazioni importanti per sempre (es. se cancelli l'unico impiegato di un dipartimento, scompare anche l'esistenza del dipartimento stesso).
3. **Anomalie di Modifica:** Se devi cambiare un dato ripetuto (es. il nome di un fornitore), devi modificarlo in centinaia di righe diverse, con il rischio di creare incongruenze se ne dimentichi qualcuna.
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
