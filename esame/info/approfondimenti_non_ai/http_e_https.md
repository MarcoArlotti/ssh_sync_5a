## HTTPS e HTTP
L'HTTP (HyperText Transfer Protocol) è il linguaggio usato nel web,
La comunicazione e' composta da un SERVER e molti client che si connettono al server,
Il funzionamento dell'HTTP è ciclico e si basa su due momenti fondamentali:
1. La Richiesta (Request): Il browser invia un messaggio al server chiedendo una risorsa specifica (un'immagine, una pagina HTML, un video).

2. La Risposta (Response): Il server invia sempre un codice di risultato, e se si ha avuto un successo il server elabora la richiesta e invia indietro il contenuto richiesto.

I vari codici (da x00 - x99) in risposta mandati dal server sono:
100. INFORMATION: TODO
200. SUCCESSO: la comunicazione e' andata a buon fine,
300. REDIRECT: la pagina e' stata spostata altrove ma il server sa dove e' stata spostata
400. ERRORE LATO CLIENT: la comunicazione non ha funzionato per colpa del client (errore 404: il client ha cercato un endpoint inesistente )
500. INTERNAL SERVER ERROR: la comunicazione e' fallita per colpa di un errore nel server.

Ad ogni nuova comunicazione http quando lo progettarono non pensarono a permettergli di mantenere uno stato durante la comunicazione quindi, essendo STATELESS ad ogni richiesta fatta dal client (GET) il server non ricorda niente da quel utente.

Per mitigare questo problema e permettere il mantenimento di un accesso ad un account anche dopo un altra richiesta GET, come soluzione si crearono i COOKIE di stato.

Il browser del client salva sulla sua memoria lo stato della connessione, ed ad ogni nuova richiesta GET, automatcamente il cookie verra' inviato insieme al GET.

Infine con l'avvento dei e-commerce, e' importante che tutti i dati ricevuti e inviati siano inviati crittografandoli,

come soluzione nacque HTTPS che usa http + TSL (Trasport Layer Security).

### Il TLS Handshake (La stretta di mano)

Prima che i dati vengano scambiati, il client e il server effettuano un "handshake" per stabilire una connessione sicura:

1. Certificato Digitale: Il server invia il suo certificato (firmato da una Certification Authority) per garantire al client di essere chi dice di essere.

2. Scambio delle chiavi: Usano la crittografia asimmetrica (chiave pubblica e privata) per concordare una "chiave di sessione" segreta.

3. Crittografia Simmetrica: Una volta stabilita la chiave di sessione, i dati della navigazione (HTML, cookie, password) vengono criptati con crittografia simmetrica, che è molto più veloce per lo scambio di grandi quantità di dati.

HTTPS non protegge solo i dati da essere in piena vista (Riservatezza), ma garantisce anche:

- Integrità: I dati non possono essere modificati da un malintenzionato durante il tragitto (attacco Man-in-the-Middle).

- Autenticazione: Hai la certezza di parlare con il server reale e non con un impostore.

## REST e API
### Le API

Un'API è un insieme di definizioni e protocolli che consentono a diverse applicazioni di comunicare tra loro.

Un'API permette di collegare un software con un altro,
permettendo che i dati e funzionalità vengano condivisi in modo sicuro e strutturato.

Le API sono molto usate per:

- Accesso a database: ad esempio, quando un'applicazione vuole recuperare dati da un sistema remoto.
- Servizi esterni: come la comunicazione tra un sito e una piattaforma di pagamento o di analisi.
- Sistemi mobili: app mobile che si interfacciano con i server backend via API.

Le API possono essere implementate in vari modi, ma uno dei modelli più diffusi è REST.

### REST
REST (REpresentational State Transfer) è un stile architetturali per progettare una API web,
con lo scopo di rendere scalabili e facili da usare le API create.

Si basa sull'uso di HTTP per permettere la comunicazione tra client e server, sfruttando i metodi di richiesta standard di HTTP (GET, POST, PUT, DELETE, ecc.) per interagire con le risorse.

I principi chiave di REST:


1. **Client-Server**: Il client e il server sono separati e indipendenti. Il client si occupa dell'interfaccia utente, il server della gestione dei dati.

2. **Stateless (Senza Stato)**: Ogni richiesta dal client al server deve contenere tutte le informazioni necessarie per essere compresa. Il server non memorizza lo stato del client tra una richiesta e l'altra.

3. **Cacheable**: Le risposte del server dovrebbero indicare se possono essere messe in cache dal client. La cache migliora le prestazioni riducendo la necessità di richieste ripetute.

4. **Uniform Interface (Interfaccia Uniforme)**: Questo è il principio chiave di REST e si basa su quattro pilastri:
    - ***Identificazione delle Risorse:*** Ogni risorsa è identificata in modo univoco da un URI (Uniform Resource Identifier), come un URL. Esempio: /utenti/123.
    - ***Manipolazione tramite Rappresentazioni:*** Il client non interagisce direttamente con la risorsa sul server, ma con una sua rappresentazione (es. un documento JSON o XML).
    - ***Messaggi Auto-Descrittivi:*** Ogni messaggio (richiesta/risposta) contiene abbastanza informazioni per descrivere come essere processato (es. l'header Content-Type: application/json dice al server di interpretare il body come JSON).
    - ***HATEOAS (Hypermedia as the Engine of Application State):*** Le risposte del server dovrebbero includere link (hypermedia) che guidano il client sulle prossime azioni possibili (es. una risposta su un utente potrebbe contenere il link per visualizzare i suoi ordini).


## endpoint
Nel contesto di una Web API, un endpoint è un URL specifico dove un'API può essere raggiunta da un'applicazione client.
È dove l'indirizzo permette di inviare una richiesta per interagire con una specifica risorsa o un insieme di risorse.
### In pratica
La combinazione di *Metodo* +***URL***.

>GET e POST sono al posto di nomi che daremo con la logica del CRUD

esempio:
`GET/utenti`
`POST/utenti`

### GET
```python
import requests
import json

#creazione dell'URL + ID
id = 1
url = f"https://jsonplaceholder.typicode.com/users/{id}"

# 1. Eseguiamo la richiesta GET
    response = requests.get(url)
```

### POST
```python
import requests
import json

# L'URL dell'endpoint per la creazione dei post
url = "https://jsonplaceholder.typicode.com/posts"

# 1. Prepariamo i dati da inviare nel corpo della richiesta.
# Deve essere un dizionario Python che verrà convertito in JSON.
nuovo_post = {
    'title': 'Il Mio Nuovo Post',
    'body': 'Questo è il contenuto del mio primo post creato tramite API!',
    'userId': 1
}

response = requests.post(url, json=nuovo_post)
# 3. Controlliamo lo status code
# Per una creazione, ci aspettiamo uno status code 201 (Created)
response.raise_for_status()

# 4. Analizziamo la risposta del server
# Di solito, l'API restituisce l'oggetto che abbiamo creato,
# con l'ID assegnato dal server
post_creato = response.json()
```
## WSGI e ASGI
## FLASK

## DBSM e NoSQL, la importanza delle query

## diagramma ER

## La Chiave Univoca, Foreing key e Primary key

## cardinalita'