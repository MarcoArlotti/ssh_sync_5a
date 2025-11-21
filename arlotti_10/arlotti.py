import requests
import json

link_todo = "https://jsonplaceholder.typicode.com/todos?userId=1"

response_todo = requests.get(link_todo)

response_todo.raise_for_status()

lista_todo = response_todo.json()

totali = 0
non_completati = 0

for todo in lista_todo:
    totali = totali + 1

    if not todo["completed"]:
        non_completati = non_completati + 1

        print(f"id {todo["userId"]}")
        print(f"id {todo["id"]}")
        print(f"title {todo["title"]}")
        print(f"completed {todo["completed"]}")
        print("------------")

        todo_id = todo["id"]
        link_da_modificare = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
        payload = todo
        response = requests.put(link_da_modificare, json=payload)

completati = totali - non_completati

print(f"totali: {totali}")
print(f"non completati: {non_completati}")
print(f"completati: {completati}")