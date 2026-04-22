# ***Architettura Web con Flask e Jinja2***

*(Arlotti, Ibragimov, Pontellini)*

---

# **Flask**

Flask è un **micro-framework web in Python**.

Caratteristiche:

* leggero
* flessibile
* modulare

Componenti:

* **Werkzeug** → gestione HTTP
* **Jinja2** → template

 Ideale per:

* API
* microservizi

---


# **Struttura App: Ruolo di `__init__.py` e Blueprint**

Quando si sviluppa una web app con Flask, è fondamentale organizzare il codice in modo **modulare e scalabile**.

### **`__init__.py`**

È il file principale dell’applicazione:

* crea l’istanza di Flask
* configura l’app (chiavi, database, ecc.)
* registra i Blueprint

Si usa spesso il **pattern Application Factory**:

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'chiave_segreta'

    from .routes import main
    app.register_blueprint(main)

    return app
```

 Vantaggi:

* supporta ambienti diversi (test, produzione)
* migliora la struttura del progetto
* facilita il testing

---

### **Blueprint**

Permettono di dividere le funzioni in piu' file separati per mantenere ordinato il codice.

Esempio:

* `auth` → login
* `main` → homepage
* `admin` → pannello admin

```python
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Homepage"
```

Registrazione:

```python
app.register_blueprint(main)
```

 Vantaggi:

* lavoro in team facilitato
* maggiore scalabilità

---

# **Frontend Dinamico: Jinja2 ed ereditarietà**

Flask utilizza **Jinja2** per generare un HTML dinamico.

### **Jinja2**

Permette di inserire dati dinamici:

```html
<h1>Ciao {{ nome }}</h1>
```

Condizioni:

```html
{% if user %}
    <p>Benvenuto {{ user }}</p>
{% endif %}
```

Cicli:

```html
{% for u in utenti %}
    <li>{{ u }}</li>
{% endfor %}
```

---

### **Ereditarietà (`{% extends %}`)**

Permette di riutilizzare layout comuni, evitando riscrivere parte di codice che si ripetera' in altri ***endpoint***

**base.html**

```html
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**index.html**

```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h1>Homepage</h1>
{% endblock %}
```

 Vantaggi:

* codice più pulito
* manutenzione semplice

---

# **Ciclo Request/Response**

Il web funziona con il modello:

 **Client → Request → Server → Response**

### **Fasi**

1. Il client invia una richiesta
2. Il server la elabora
3. Il server restituisce una risposta

### **Status Code**

* **200 OK** → successo
* **201 Created** → risorsa creata
* **302 Redirect** → reindirizzamento
* **400 Bad Request** → errore client
* **404 Not Found** → risorsa inesistente
* **500 Internal Server Error** → errore server

---

# **GET vs POST**

| GET                | POST            |
| ------------------ | --------------- |
| recupera dati      | invia dati      |
| parametri nell’URL | dati nel body   |
| idempotente        | non idempotente |
| cacheabile         | non cacheabile  |

 **GET = leggere**
 **POST = scrivere**

---

# **HTTP e HTTPS**

### **HTTP**

È il protocollo usato nel web per comunicare tra client e server.

* È **stateless** → il server non ricorda le richieste precedenti
* Funziona con request/response



### **Cookie e Sessioni**

Per mantenere lo stato:

* il server invia un **cookie**
* il browser lo salva
* lo reinvia ad ogni richiesta

 Permette login, carrelli, ecc.



### **HTTPS**

È HTTP + **TLS (Transport Layer Security)**

 Serve per:

* proteggere i dati
* evitare intercettazioni
* garantire autenticità



### **TLS Handshake**

1. Il server invia il certificato
2. Viene verificata l’identità
3. Si crea una chiave di sessione
4. I dati vengono cifrati



### **Sicurezza garantita**

* **Riservatezza** → dati criptati
* **Integrità** → dati non modificabili
* **Autenticazione** → server verificato

---

# **REST e API**

### **API**

Un’API permette a due software di comunicare.

Esempi:

* app mobile ↔ server
* sito ↔ sistema di pagamento



### **REST**

È uno stile per progettare API.

Principi:

1. **Client-Server** → separazione
2. **Stateless** → nessuna memoria lato server
3. **Cacheable** → miglior performance
4. **Uniform Interface** → regole standard

---

### **Endpoint**

Un endpoint è:

 **Metodo + URL**

Esempi:

```
GET /utenti
POST /utenti
```

---

# **WSGI e ASGI**

### **Problema**

Il web server non sa eseguire Python → serve un intermediario



### **WSGI**

* standard classico
* sincrono
* una richiesta alla volta

Esempio: **Gunicorn**



### **ASGI**

* supporta `async/await`
* gestisce molte richieste contemporaneamente
* supporta WebSocket

Esempi:

* FastAPI
* Uvicorn

---
# **Database (DBMS e NoSQL)**

### **DBMS (Relazionali)**

* dati in tabelle
* uso di SQL
* relazioni tra dati

Esempi:

* MySQL
* PostgreSQL

---

### **NoSQL**

* dati non strutturati
* più flessibili
* scalabilità elevata

Esempi:

* MongoDB


### **Importanza delle query**

Le query servono per:

* leggere dati
* inserire dati
* aggiornare dati
* eliminare dati


## **Diagramma ER**

Il diagramma Entity-Relationship rappresenta:

* entità (tabelle)
* attributi (colonne)
* relazioni

Esempio:

* Utente → Ordine


---

### **Primary Key**

* identifica un record in modo univoco
* es: ID utente


### **Foreign Key**

* collega due tabelle
* es: utente_id negli ordini