Panoramica

Questo script Python fa una richiesta HTTP GET a un'API di prova (jsonplaceholder) per recuperare i dati di un utente (user_id = 3), converte la risposta JSON in un dizionario Python e stampa i dati completi e alcune informazioni specifiche (nome, email, città). Gestisce gli errori di rete e gli errori HTTP in modo semplice.
Sequenza principale di operazioni

    Definizione dell'endpoint con l'ID utente.

    Invio della richiesta GET con requests.get..

    Verifica dello status della risposta con response.raise_for_status.

    Parsing del corpo JSON in un dizionario Python con response.json().

    Stampa del dizionario in formato "pretty" usando json.dumps(indent=4).

    Estrazione e stampa di campi specifici: name, email, address.city..

    Gestione delle eccezioni per errori HTTP e generici di richiesta.

Spiegazione riga per riga (punti chiave)

    import requests / import json Importano le librerie: requests per le richieste HTTP, json per lavorare con JSON e formattare l'output.

    user_id = 3 Variabile che decide quale utente richiedere; viene inserita nell'URL.

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}" Costruisce l'URL finale usando una f-string.

    response = requests.get(url) Invia la richiesta HTTP GET e memorizza la risposta nell'oggetto response.

    response.raise_for_status() Se lo status code è 4xx o 5xx, solleva requests.exceptions.HTTPError; questo fa saltare il flusso al blocco except.

    dati_utente = response.json() Converte automaticamente il corpo JSON in un dizionario Python.

    print(json.dumps(dati_utente, indent=4)) Stampa il dizionario in modo leggibile (indentazione).

    print(f"Nome: {dati_utente['name']}") ecc. Accede a chiavi del dizionario per mostrare valori specifici; per la città usa la chiave annidata address['city'].

    except requests.exceptions.HTTPError as err / except requests.exceptions.RequestException as err Gestione degli errori: il primo cattura errori HTTP; il secondo cattura qualsiasi altra eccezione legata alla richiesta (timeout, DNS, connessione).

Possibili errori comuni e consigli pratici

    KeyError se la struttura JSON non contiene le chiavi attese. Per evitare crash usare dati_utente.get('name') o controlli con in.

    Timeout non gestito esplicitamente. Si può passare timeout alla get: requests.get(url, timeout=5).

    Nessuna verifica del contenuto: se la risposta non è JSON .json() può sollevare ValueError; si può controllare response.headers['Content-Type'] prima.

    Per debug/registrazione, usare logging invece di print.

Miglioramenti suggeriti (rapidi)

    Aggiungere timeout: requests.get(url, timeout=5).

    Usare .get per estrazioni sicure: dati_utente.get('name', 'N/A').

    Gestire ValueError per .json() in caso di risposta non valida.

    Parametrizzare user_id o prendere input dall'utente in modo sicuro.

