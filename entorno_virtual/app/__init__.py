from flask import Flask
import pymysql
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Conexión MySQL
    connection = pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        db=Config.MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    app.connection = connection

    # Blueprints
    from .controllers.compras_controller import compras_bp
    from .controllers.main_controller import main_bp
    from .controllers.user_controller import user_bp

    app.register_blueprint(compras_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app
