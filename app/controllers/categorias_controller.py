from flask import Blueprint, render_template, request, redirect, url_for, current_app

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categoria")
            categorias = cursor.fetchall()
        return render_template('admin/categorias.html', categorias=categorias)
    except Exception as e:
        return str(e)



@categoria_bp.route('/categorias/agregar', methods=['POST'])
def agregar_categoria():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO categoria (nombre_categoria, descripcion_categoria) VALUES (%s, %s)", (nombre, descripcion))
        connection.commit()
    return redirect(url_for('categoria_bp.listar_categorias'))


@categoria_bp.route('/categorias/editar/<int:id>', methods=['POST'])
def editar_categoria(id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("UPDATE categoria SET nombre_categoria = %s, descripcion_categoria = %s WHERE id_categoria = %s", (nombre, descripcion, id))
        connection.commit()
    return redirect(url_for('categoria_bp.listar_categorias'))


@categoria_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_categoria(id):
    print(f"Intentando eliminar ID: {id}")  # Debug temporal
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (id,))
        connection.commit()
    return redirect(url_for('categoria_bp.listar_categorias'))



