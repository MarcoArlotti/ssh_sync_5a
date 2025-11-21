import requests
import json

# Definiamo l'URL dell'endpoint a cui vogliamo fare la richiesta
user_id = 1
post_id = 1
user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
post = "https://jsonplaceholder.typicode.com/posts"
post_post_id_comments = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
try:
    # 1. Eseguiamo la richiesta GET
    response = requests.get(user)
    response3 = requests.get(post_post_id_comments)
    response4 = requests.get(post)
    # 2. Controlliamo se la richiesta è andata a buon fine (status code 200 OK)
    response.raise_for_status()  # Solleva un'eccezione per status code 4xx o 5x
    response3.raise_for_status()
    response4.raise_for_status()
    # 3. Estraiamo i dati JSON dalla risposta
    # Il metodo .json() converte automaticamente il corpo della risposta da stringa JSON a dizionario Python
    dati_utente = response.json()
    commenti_per_post_id = response3.json()
    tutti_post = response4.json()

    id_propietario_post = dati_post['userId']
    print("1 --")
    for i in tutti_post:
        if i['userId'] == id_propietario_post:
            print(f"propietario: {i['userId']}")
            print(f"id post: {i['id']}")
            print(f"titolo: {i['title']}")
            print(f"corpo: {i['body']}")
            print()

    # print(f"ID utente: {dati_post['userId']}")
    print("2 --")

    for i in commenti_per_post_id:
        if i['postId'] == post_id:
            print(f"post: {i['postId']}")
            print(f"id: {i['id']}")
            print(f"name: {i['name']}")
            print(f"email: {i['email']}")
            print(f"body:{i["body"]}")
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