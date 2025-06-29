from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    application = Flask(__name__)
    application.config.from_pyfile('config.py')

    db.init_app(application)
    migrate.init_app(application, db)

    from app.routes import bp

    application.register_blueprint(bp)

    import app.models

    return application