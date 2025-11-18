import requests
import json

# Definiamo l'URL dell'endpoint a cui vogliamo fare la richiesta
user_id = 1
url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

try:
    # 1. Eseguiamo la richiesta GET
    response = requests.get(url)

    # 2. Controlliamo se la richiesta è andata a buon fine (status code 200 OK)
    response.raise_for_status()  # Solleva un'eccezione per status code 4xx o 5xx

    # 3. Estraiamo i dati JSON dalla risposta
    # Il metodo .json() converte automaticamente il corpo della risposta da stringa JSON a dizionario Python
    dati_utente = response.json()

    # 4. Usiamo i dati
    print("--- Dati Utente Ricevuti ---")
    # Usiamo json.dumps per una stampa "bella" (pretty-print) del dizionario
    print(json.dumps(dati_utente, indent=4))

    print("\n--- Informazioni Specifiche ---")
    print(f"Nome: {dati_utente['name']}")
    print(f"Email: {dati_utente['email']}")
    print(f"Città: {dati_utente['address']['city']}")

except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")

"""
--- Post dell'utente 1 ---
ID Post: 1, Titolo: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
ID Post: 2, Titolo: qui est esse
ID Post: 3, Titolo: ea molestias quasi exercitationem repellat qui ipsa sit aut

--- Commenti per il primo post ---
- id labore ex et quam laborum: laudantium enim quasi est quidem magnam voluptate ipsam eos
- quo vero reiciendis velit similique earum: est natus enim nihil est dolore omnis voluptatem numquam

--- Nuovo Commento Creato ---
{
    "postId": 1,
    "id": 501,
    "name": "Nuovo Commentatore",
    "email": "nuovo@example.com",
    "body": "Questo è un commento aggiunto tramite API!"
}
"""