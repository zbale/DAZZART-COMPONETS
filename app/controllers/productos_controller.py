from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
import pymysql

producto_bp = Blueprint('producto_bp', __name__)

# Ruta para agregar un nuevo producto
@producto_bp.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    img_folder = os.path.join(current_app.root_path, 'static', 'IMG')
    imagenes = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]

    connection = current_app.connection

    if request.method == 'POST':
        numero_serial = request.form['numero_serial']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']
        fecha_creacion = request.form['fecha_creacion']

        # Manejo de imagen seleccionada o nueva subida
        imagen_seleccionada = request.form.get('imagen')
        imagen_subida = request.files.get('imagen_subida')

        imagen_filename = None
        if imagen_subida and imagen_subida.filename:
            imagen_filename = secure_filename(imagen_subida.filename)
            imagen_subida.save(os.path.join(img_folder, imagen_filename))
        elif imagen_seleccionada:
            imagen_filename = imagen_seleccionada

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO producto (numero_serial, nombre, descripcion, precio, stock, id_categoria, fecha_creacion, imagen)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (numero_serial, nombre, descripcion, precio, stock, id_categoria, fecha_creacion, imagen_filename))
                connection.commit()
                flash('Producto agregado correctamente', 'success')
        except Exception as e:
            connection.rollback()
            flash(f'Error al agregar producto: {e}', 'danger')

        return redirect(url_for('producto_bp.listar_productos'))

    # Cargar categorías
    categorias = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria")
            categorias = cursor.fetchall()
    except Exception as e:
        flash(f'Error al obtener categorías: {e}', 'danger')

    return render_template('Admin/añadirproducto.html', categorias=categorias, imagenes=imagenes)


# Ruta para listar todos los productos
@producto_bp.route('/productos')
def listar_productos():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM producto")
            productos = cursor.fetchall()
    except Exception as e:
        flash(f'Error al obtener productos: {e}', 'danger')

    # Obtener imágenes disponibles
    img_folder = os.path.join(current_app.root_path, 'static', 'IMG')
    imagenes = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]

    return render_template('Admin/productos.html', productos=productos, imagenes=imagenes)


# Ruta para editar un producto existente
@producto_bp.route('/productos/editar/<int:id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    connection = current_app.connection
    img_folder = os.path.join(current_app.root_path, 'static', 'IMG')
    imagenes = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]

    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
            producto = cursor.fetchone()

            cursor.execute("SELECT * FROM categoria")
            categorias = cursor.fetchall()

        return render_template('Admin/actualizarpro.html', producto=producto, categorias=categorias, imagenes=imagenes)

    if request.method == 'POST':
        numero_serial = request.form['numero_serial']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']

        imagen_seleccionada = request.form.get('imagen')
        imagen_subida = request.files.get('imagen_subida')

        if imagen_subida and imagen_subida.filename:
            imagen_filename = secure_filename(imagen_subida.filename)
            imagen_subida.save(os.path.join(img_folder, imagen_filename))
        elif imagen_seleccionada:
            imagen_filename = imagen_seleccionada
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT imagen FROM producto WHERE id_producto = %s", (id_producto,))
                producto_actual = cursor.fetchone()
                imagen_filename = producto_actual['imagen'] if producto_actual else None

        with connection.cursor() as cursor:
            query = """
                UPDATE producto
                SET numero_serial = %s, nombre = %s, descripcion = %s, precio = %s, 
                    stock = %s, id_categoria = %s, imagen = %s
                WHERE id_producto = %s
            """
            cursor.execute(query, (numero_serial, nombre, descripcion, precio, stock, id_categoria, imagen_filename, id_producto))
            connection.commit()

        flash('Producto actualizado correctamente', 'success')
        return redirect(url_for('producto_bp.listar_productos'))


# Ruta para eliminar un producto
@producto_bp.route('/productos/eliminar/<int:id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT imagen FROM producto WHERE id_producto = %s", (id_producto,))
            producto = cursor.fetchone()
            if producto and producto['imagen']:
                imagen_path = os.path.join(current_app.root_path, 'static', 'IMG', producto['imagen'])
                if os.path.exists(imagen_path):
                    os.remove(imagen_path)
            cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
            connection.commit()
            flash('Producto eliminado correctamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar producto: {e}', 'danger')

    return redirect(url_for('producto_bp.listar_productos'))


# Ruta para servir imágenes desde la carpeta estática
@producto_bp.route('/img/<filename>')
def serve_image(filename):
    img_folder = os.path.join(current_app.root_path, 'static', 'IMG')
    if os.path.exists(os.path.join(img_folder, filename)):
        return send_from_directory(img_folder, filename)
    else:
        return "Imagen no encontrada", 404
