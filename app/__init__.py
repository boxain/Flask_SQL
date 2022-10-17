from flask import Flask
from .config import configs
from .database import db


def create_app(env):
    
    app = Flask(__name__,template_folder="../templates",static_folder="../static")
    app.config.from_object(configs[env])
    db.init_app(app=app)

    from .course import course_bp
    from .main import main_bp
    from .user import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(user_bp)    

    return app

