import os
from flask import Flask,render_template

def create_app():
    # 1. Creiamo l'istanza di Flask
    # instance_relative_config=True dice a Flask: 
    # "Cerca la cartella 'instance' fuori da 'app', non dentro."
    app = Flask(__name__, instance_relative_config=True)

    # 2. Configurazione di base
    # Qui impostiamo le variabili fondamentali.
    app.config.from_mapping(
        # SECRET_KEY serve a Flask per firmare i dati sicuri (es. sessioni).
        # 'dev' va bene per sviluppare, ma in produzione andrà cambiata.
        SECRET_KEY='dev',
        # Diciamo a Flask dove salvare il file del database SQLite
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )

    # 3. Assicuriamoci che la cartella 'instance' esista fisicamente.
    # Se non esiste (es. è la prima volta che avvii), Flask la crea.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def hello():
        title = "Pagina Principale"
        message = "we"
        name = "FABIO"
        return render_template('home.html', title=title, message=message, name=name)
    return app

    @app.route('/todo')
    def todo():
        title = "todo"
        message = "benvenuto nei todo"
        name = "FABIO"
        return render_template('todo.html', title=title, message=message, name=name)
    return app