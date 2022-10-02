from flask import Flask
from .config import configs
from .database import db


def create_app(env):
    
    app = Flask(__name__,template_folder="../templates",static_folder="../static")
    app.config.from_object(configs[env])
    db.init_app(app=app)

    return app

