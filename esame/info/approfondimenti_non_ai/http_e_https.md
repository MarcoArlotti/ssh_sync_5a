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

## endpoint

## FLASK

## DBSM e NoSQL, la importanza delle query

## diagramma ER

## La Chiave Univoca, Foreing key e Primary key

## cardinalita'