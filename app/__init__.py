#Este código establece la conexión con la base de datos utilizando PyMySQL
from flask import Flask
import pymysql.cursors
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configuración de la conexión a la base de datos
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )
    
    # Importar y registrar los blueprints
    from app.controllers.main_controller import main_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.categorias_controller import categoria_bp
    from app.controllers.subcategorias_controller import subcategoria_bp
    from app.controllers.productos_controller import producto_bp
    from app.controllers.descuento_controller import descuento_bp
    from app.controllers.pedidos_admin_controller_ import admin_bp as pedidos_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(subcategoria_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(descuento_bp)
    app.register_blueprint(pedidos_bp, url_prefix='/admin') 



    # Agregar la conexión a la base de datos como un atributo de la aplicación
    app.connection = connection

    return app

    #return app