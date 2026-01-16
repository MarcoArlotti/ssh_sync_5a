import os
from flask import Flask, render_template

from app.repository.canali_repositories import get_channel
from app.repository.video_repositories import get_videos
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
        DATABASE=os.path.join(app.instance_path, 'video.db'),
    )

    # 3. Assicuriamoci che la cartella 'instance' esista fisicamente.
    # Se non esiste (es. è la prima volta che avvii), Flask la crea.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 4. Una route di prova per vedere se funziona
    @app.route('/')
    def index():
        channels_py = get_channel()
        return render_template("index.html", channels_html=channels_py)

    @app.route('/channel/<int:canale_id>')
    def channel(canale_id):
        video_py = get_videos(canale_id)
        return render_template("channel.html",videos_html=video_py)
    return app