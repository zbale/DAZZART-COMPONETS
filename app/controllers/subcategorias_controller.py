from flask import Blueprint, render_template, request, redirect, url_for, current_app
from collections import defaultdict


subcategoria_bp = Blueprint('subcategoria_bp', __name__)

@subcategoria_bp.route('/subcategorias', methods=['GET'])
def listar_subcategorias():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            # Obtener subcategorías y sus categorías
            cursor.execute("""
                SELECT s.id_subcategoria, s.nombre_subcategoria, s.descripcion_subcategoria,
                       c.id_categoria, c.nombre_categoria
                FROM subcategoria s
                JOIN categoria c ON s.id_categoria = c.id_categoria
            """)
            subcategorias = cursor.fetchall()

            # Agrupar por categoría
            subcategorias_por_categoria = defaultdict(list)
            for row in subcategorias:
                subcategorias_por_categoria[row['nombre_categoria']].append(row)

            # Obtener categorías para el formulario
            cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria")
            categorias = cursor.fetchall()

        return render_template(
            'admin/subcategorias.html',
            subcategorias_por_categoria=subcategorias_por_categoria,
            categorias=categorias  # <-- se pasa al template
        )
    except Exception as e:
        return f"Error: {str(e)}"

@subcategoria_bp.route('/subcategorias/agregar', methods=['POST'])
def agregar_subcategoria():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    id_categoria = request.form['id_categoria']  # Asegúrate de enviar este valor si hay relación

    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO subcategoria (nombre_subcategoria, descripcion_subcategoria, id_categoria) VALUES (%s, %s, %s)",
            (nombre, descripcion, id_categoria)
        )
        connection.commit()
    return redirect(url_for('subcategoria_bp.listar_subcategorias'))

@subcategoria_bp.route('/subcategorias/editar/<int:id>', methods=['POST'])
def editar_subcategoria(id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    id_categoria = request.form['id_categoria']

    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE subcategoria SET nombre_subcategoria = %s, descripcion_subcategoria = %s, id_categoria = %s WHERE id_subcategoria = %s",
            (nombre, descripcion, id_categoria, id)
        )
        connection.commit()
    return redirect(url_for('subcategoria_bp.listar_subcategorias'))

@subcategoria_bp.route('/subcategorias/eliminar/<int:id>', methods=['POST'])
def eliminar_subcategoria(id):
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM subcategoria WHERE id_subcategoria = %s", (id,))
        connection.commit()
    return redirect(url_for('subcategoria_bp.listar_subcategorias'))
