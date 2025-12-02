import requests


def prendi_dati_link(link):
    risposta = requests.get(link)
    risposta.raise_for_status()
    lista = risposta.json()
    return risposta,lista

def stampa_un_dizionario(dizionario):
    for chiave, valore in dizionario.items():
        print(f"{chiave}: {valore}")
