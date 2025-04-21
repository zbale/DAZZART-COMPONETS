from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash

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

@categoria_bp.route('/categorias/eliminar/<int:id>', methods=['POST'])
def eliminar_categoria(id):
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (id,))
        connection.commit()
    return redirect(url_for('categoria_bp.listar_categorias'))

descuento_categoria_bp = Blueprint('descuento_categoria_bp', __name__)

@descuento_categoria_bp.route('/descuentocategoria', methods=['GET'])
def descuentos_categoria():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            # Consulta para obtener los datos necesarios
            query = """
                SELECT d.id_descuento, c.nombre_categoria, d.porcentaje, d.fecha_inicio, d.fecha_fin, d.estado_descuento
                FROM descuento d
                JOIN categoria c ON d.id_categoria = c.id_categoria
            """
            cursor.execute(query)
            descuentos = cursor.fetchall()
        return render_template('Admin/descuentocategoria.html', descuentos=descuentos)
    except Exception as e:
        print("Error al obtener descuentos por categoría:", e)
        return render_template('Admin/descuentocategoria.html', descuentos=[])

@descuento_categoria_bp.route('/descuentocategoria/agregar', methods=['POST'])
def agregar_descuento_categoria():
    connection = current_app.connection
    try:
        id_categoria = request.form.get('id_categoria')
        porcentaje = request.form.get('porcentaje')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        estado = request.form.get('estado')

        if not id_categoria or not porcentaje or not fecha_inicio or not fecha_fin or not estado:
            flash('Todos los campos son obligatorios.', 'danger')
            return redirect(url_for('descuento_categoria_bp.descuentos_categoria'))

        with connection.cursor() as cursor:
            query = """
                INSERT INTO descuento (id_categoria, porcentaje, fecha_inicio, fecha_fin, estado_descuento)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (id_categoria, porcentaje, fecha_inicio, fecha_fin, estado))
            connection.commit()

        flash('Descuento agregado correctamente.', 'success')
    except Exception as e:
        print("Error al agregar descuento por categoría:", e)
        flash('Error al agregar el descuento.', 'danger')

    return redirect(url_for('descuento_categoria_bp.descuentos_categoria'))



