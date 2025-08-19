from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # register blueprints
    from .routes.main import main_bp
    from .routes.trades import trades_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(trades_bp, url_prefix="/trades")

    return app
