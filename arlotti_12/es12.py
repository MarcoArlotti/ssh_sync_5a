import requests


# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# python -m venv .venv  
# .venv\Scripts\Activate.ps1
# python.exe -m pip install --upgrade pip
# pip install requests
# in caso windows rompe

# omarchy

id = 1
# il cazzo di link
link_author_id = f"http://localhost:4070/books/?author_id={id}"

# quel che devi fare aka prendere dati
response_author_id = requests.get(link_author_id)

# controllo degli errori
response_author_id.raise_for_status()

# conversione in un linguaggio leggibile
lista_response_author_id = response_author_id.json()

# metodo che ti da 2
print(lista_response_author_id)

# metodo bello
for autori in lista_response_author_id:
    print("------------------------")
    print(f"title: {autori['title']}")
    print(f"pages: {autori['pages']}")
    print("\\\\\\\\\\\\\\\\\\\\\\\\")

# metodo post
# id = 23
# il cazzo di link
# link_author_id = "http://localhost:4070/books/authors/id=23"
# 
# dizionario_nuovo = {
    # "id": 23,
    # "author_id": 23,
    # "genre_id": 23,
    # "title": "casali",
    # "pages": 23,
    # "available": True
    # }
# 
# 
# response = requests.post(link_author_id, json=dizionario_nuovo)
# 
# print(response.status_code)   # codice di stato HTTP (200 = OK)
# print(response.text)    

# il cazzo di link
link_authors = "http://localhost:4070/books/authors"

# quel che devi fare aka prendere dati
response_authors = requests.get(link_authors)

# controllo degli errori
response_authors.raise_for_status()

# conversione in un linguaggio leggibile
lista_response_authors = response_authors.json()
print("\nlibri disponibili:\n")
contatore = 0
for autore in lista_response_authors:
    if autore['available']:
        print(f"titolo: {autore['title']}")
        
        pagine = autore['pages']
        contatore = contatore + pagine

print(f"pagine totali: {contatore}")


id = 101
# il cazzo di link
link_books = "http://localhost:4070/books"

# quel che devi fare aka prendere dati
response_books = requests.get(link_books)

# controllo degli errori
response_books.raise_for_status()

# conversione in un linguaggio leggibile
lista_response_books = response_books.json()

contatore = 0
print("\nlibri per genere:\n")
for libro in lista_response_books:
    if libro['genre_id'] == id:
        print("|||||||||||||||||||||||||||||")
        print(f"id: {libro['id']}")
        print(f"author_id: {libro['author_id']}")
        print(f"genre_id: {libro['genre_id']}")
        print(f"title: {libro['title']}")
        print(f"pages: {libro['pages']}")
        print(f"available: {libro['available']}")
        print("///////////////////////////")
        contatore = contatore + 1
print(f"libri per genere: {contatore}")