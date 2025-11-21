import requests
import json

# Definiamo l'URL dell'endpoint a cui vogliamo fare la richiesta
user_id = 1
post_id = 1
url1 = f"https://jsonplaceholder.typicode.com/users/{user_id}"
url2 = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
url3 = "https://jsonplaceholder.typicode.com/posts"
url3 = "https://jsonplaceholder.typicode.com/posts"
try:
    # 1. Eseguiamo la richiesta GET
    response = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    # 2. Controlliamo se la richiesta è andata a buon fine (status code 200 OK)
    response.raise_for_status()  # Solleva un'eccezione per status code 4xx o 5xx
    response2.raise_for_status()
    response3.raise_for_status()
    # 3. Estraiamo i dati JSON dalla risposta
    # Il metodo .json() converte automaticamente il corpo della risposta da stringa JSON a dizionario Python
    dati_utente = response.json()
    dati_post = response2.json()
    tutti_post = response3.json()

    for i in tutti_post:
        if i['userId'] == tutti_post:
            print(f"propietario: {i['userId']}")
            print(f"id post: {i['id']}")
            print(f"titolo: {i['title']}")
            print(f"corpo: {i['body']}")
            print()
    # print(f"ID utente: {dati_post['userId']}")
    id_propietario_post = dati_post['userId']
    for i in tutti_post:
        if i['userId'] == id_propietario_post:
            print(f"propietario: {i['userId']}")
            print(f"id post: {i['id']}")
            print(f"titolo: {i['title']}")
            print(f"corpo: {i['body']}")
            print()
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