import os
import flask
from flask import Flask
from . import logica_database
def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev",DATABASE=os.path.join(app.instance_path,"pagina_login.sqlite"))

logica_database.fai_partire(app)