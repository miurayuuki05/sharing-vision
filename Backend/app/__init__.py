import os
from flask import Flask
from app.config import Config
from app.routes import main
from app.model import Article
from app.database import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app)
    
    # Configuration settings
    app.config.from_object(Config)
    app.register_blueprint(main)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

