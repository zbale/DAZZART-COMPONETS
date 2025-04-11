from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_bcrypt import Bcrypt
from flask import session
import os


producto_bp = Blueprint('producto_bp', __name__)

from flask import render_template, request, redirect, url_for, flash, current_app
import pymysql


@producto_bp.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # Recuperamos los datos del formulario
        numero_serial = request.form['numero_serial']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']
        fecha_creacion = request.form['fecha_creacion']

        # Insertamos el nuevo producto en la base de datos
        connection = current_app.connection  # Suponiendo que tienes configurada la conexión
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO producto (numero_serial, nombre, descripcion, precio, stock, id_categoria, fecha_creacion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (numero_serial, nombre, descripcion, precio, stock, id_categoria, fecha_creacion))
                connection.commit()
                flash('Producto agregado correctamente', 'success')
        except Exception as e:
            flash(f'Error al agregar producto: {e}', 'danger')
            connection.rollback()

            return redirect(url_for('producto_bp.listar_productos'))

    # Obtener las categorías desde la base de datos (ajusta esto según tu estructura de base de datos)
    connection = current_app.connection
    categorias = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria")  # Ajusta la consulta según tu tabla y columnas
            categorias = cursor.fetchall()  # Obtenemos todas las categorías
    except Exception as e:
        flash(f'Error al obtener categorías: {e}', 'danger')

    # Pasamos las categorías al template
    return render_template('Admin/añadirproducto.html', categorias=categorias)


@producto_bp.route('/productos')
def listar_productos():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM producto")
            productos = cursor.fetchall()
    except Exception as e:
        flash(f'Error al obtener productos: {e}', 'danger')

    return render_template('Admin/productos.html', productos=productos)


@producto_bp.route('/productos/editar/<int:id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    connection = current_app.connection
    # Si el método es GET, obtenemos el producto y las categorías
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
            producto = cursor.fetchone()  # Recupera un solo producto

            # Obtener todas las categorías para mostrar en el formulario
            cursor.execute("SELECT * FROM categoria")
            categorias = cursor.fetchall()  # Recupera todas las categorías

        # Pasar el producto y las categorías al template
        return render_template('Admin/actualizarpro.html', producto=producto, categorias=categorias)

    # Si el método es POST, procesamos la actualización
    if request.method == 'POST':
        numero_serial = request.form['numero_serial']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']
        imagen = request.files['imagen']  # Puede que necesites gestionar la carga de archivos

        # Verificar si se subió una nueva imagen
        if imagen:
            # Asegurarse de que la carpeta 'static/IMG/' exista
            images_folder = os.path.join(current_app.root_path, 'static', 'IMG')
            if not os.path.exists(images_folder):
                os.makedirs(images_folder)  # Crear la carpeta si no existe

            imagen_filename = imagen.filename
            imagen.save(os.path.join(images_folder, imagen_filename))  # Guardar imagen en la carpeta

        with connection.cursor() as cursor:
            # Actualizar el producto en la base de datos
            query = """
                UPDATE producto
                SET numero_serial = %s, nombre = %s, descripcion = %s, precio = %s, 
                    stock = %s, id_categoria = %s, imagen = %s
                WHERE id_producto = %s
            """
            cursor.execute(query, (numero_serial, nombre, descripcion, precio, stock, id_categoria, imagen_filename, id_producto))
            connection.commit()

        return redirect(url_for('producto_bp.listar_productos'))

@producto_bp.route('/productos/editar/<int:id_producto>', methods=['POST'])
def actualizar_producto(id_producto):
    # Recuperamos los datos del formulario de actualización
    numero_serial = request.form['numero_serial']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    stock = request.form['stock']
    id_categoria = request.form['id_categoria']
    fecha_creacion = request.form['fecha_creacion']

    # Realizamos la actualización en la base de datos
    query = """
        UPDATE producto SET
            numero_serial=%s,
            nombre=%s,
            descripcion=%s,
            precio=%s,
            stock=%s,
            id_categoria=%s,
            fecha_creacion=%s
        WHERE id_producto=%s
    """
    params = (numero_serial, nombre, descripcion, precio, stock, id_categoria, fecha_creacion, id_producto)

    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            flash('Producto actualizado correctamente', 'success')
    except Exception as e:
        flash(f'Error al actualizar producto: {e}', 'danger')

    return redirect(url_for('producto_bp.listar_productos'))


@producto_bp.route('/productos/eliminar/<int:id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
            connection.commit()
            flash('Producto eliminado correctamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar producto: {e}', 'danger')

    return redirect(url_for('producto_bp.listar_productos'))