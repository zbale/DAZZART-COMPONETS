from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash

descuento_bp = Blueprint('descuento_bp', __name__)
@descuento_bp.route('/admin/formulario_descuento', methods=["GET", "POST"])
def formulario_descuento():
    connection = current_app.connection
    with connection.cursor() as cursor:
        # Obtener todas las categorías
        cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria")
        categorias = cursor.fetchall()

        # Obtener todos los productos para el datalist
        cursor.execute("SELECT DISTINCT id_producto, nombre FROM producto")
        productos = cursor.fetchall()

    # Eliminar duplicados por nombre
    productos = list({p['nombre']: p for p in productos}.values())

    if request.method == 'POST':
        tipo = request.form['tipo_descuento']
        valor = request.form['valor']
        inicio = request.form['fecha_inicio']
        fin = request.form['fecha_fin']
        estado = request.form['estado_descuento']
        aplicacion = request.form['aplicacion']

        with connection.cursor() as cursor:
            # Validar si ya existe un descuento activo
            if aplicacion == 'producto':
                nombre_producto = request.form['nombre_producto']
                cursor.execute("SELECT id_producto FROM producto WHERE nombre = %s", (nombre_producto,))
                producto = cursor.fetchone()

                if not producto:
                    flash("Producto no encontrado.", "danger")
                    return redirect(request.url)

                cursor.execute("""
                    SELECT 1 FROM descuento d
                    JOIN descuento_producto dp ON d.id_descuento = dp.id_descuento
                    WHERE dp.id_producto = %s AND d.estado_descuento = 'Activo'
                """, (producto['id_producto'],))
                if cursor.fetchone():
                    flash("Ya existe un descuento activo para este producto.", "warning")
                    return redirect(request.url)

            elif aplicacion == 'categoria':
                id_categoria = request.form['id_categoria']
                cursor.execute("""
                    SELECT 1 FROM descuento d
                    JOIN descuento_categoria dc ON d.id_descuento = dc.id_descuento
                    WHERE dc.id_categoria = %s AND d.estado_descuento = 'Activo'
                """, (id_categoria,))
                if cursor.fetchone():
                    flash("Ya existe un descuento activo para esta categoría.", "warning")
                    return redirect(request.url)

            # Insertar en la tabla principal de descuentos
            cursor.execute("""
                INSERT INTO descuento (tipo_descuento, valor, fecha_inicio, fecha_fin, estado_descuento, aplicacion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (tipo, valor, inicio, fin, estado, aplicacion))

            id_descuento = cursor.lastrowid

            # Insertar en tabla intermedia
            if aplicacion == 'producto':
                cursor.execute("""
                    INSERT INTO descuento_producto (id_descuento, id_producto)
                    VALUES (%s, %s)
                """, (id_descuento, producto['id_producto']))

            elif aplicacion == 'categoria':
                cursor.execute("""
                    INSERT INTO descuento_categoria (id_descuento, id_categoria)
                    VALUES (%s, %s)
                """, (id_descuento, id_categoria))

        connection.commit()
        flash("Descuento creado correctamente.", "success")
        return redirect(url_for('descuento_bp.descuentos'))

    return render_template('Admin/formulariodescuento.html', categorias=categorias, productos=productos)

@descuento_bp.route('/admin/descuentos')
def descuentos():
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT d.id_descuento, d.tipo_descuento, d.valor, d.fecha_inicio, d.fecha_fin,
                   d.estado_descuento, d.aplicacion,
                   p.nombre AS nombre_producto,
                   c.nombre_categoria AS nombre_categoria
            FROM descuento d
            LEFT JOIN descuento_producto dp ON d.id_descuento = dp.id_descuento
            LEFT JOIN producto p ON dp.id_producto = p.id_producto
            LEFT JOIN descuento_categoria dc ON d.id_descuento = dc.id_descuento
            LEFT JOIN categoria c ON dc.id_categoria = c.id_categoria
        """)
        descuentos = cursor.fetchall()

    return render_template('Admin/descuento.html', descuentos=descuentos)

@descuento_bp.route('/descuentos/eliminar/<int:id_descuento>', methods=['POST'])
def eliminar_descuento(id_descuento):
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            # Borrar de tablas intermedias primero por las claves foráneas
            cursor.execute("DELETE FROM descuento_producto WHERE id_descuento = %s", (id_descuento,))
            cursor.execute("DELETE FROM descuento_categoria WHERE id_descuento = %s", (id_descuento,))
            # Luego borrar de la tabla principal
            cursor.execute("DELETE FROM descuento WHERE id_descuento = %s", (id_descuento,))
            connection.commit()
            flash('Descuento eliminado correctamente.', 'success')
    except Exception as e:
        print("Error al eliminar descuento:", e)
        flash('Error al eliminar descuento.', 'danger')

    return redirect(url_for('descuento_bp.descuentos'))

@descuento_bp.route('/descuentos/editar/<int:id_descuento>', methods=['GET', 'POST'])
def editar_descuento(id_descuento):
    connection = current_app.connection

    if request.method == 'POST':
        tipo_descuento = request.form['tipo_descuento']
        valor = request.form['valor']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        estado = request.form['estado_descuento']

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE descuento
                SET tipo_descuento = %s,
                    valor = %s,
                    fecha_inicio = %s,
                    fecha_fin = %s,
                    estado_descuento = %s
                WHERE id_descuento = %s
            """, (tipo_descuento, valor, fecha_inicio, fecha_fin, estado, id_descuento))
            connection.commit()
            flash('Descuento actualizado correctamente.', 'success')
            return redirect(url_for('descuento_bp.descuentos'))

    # GET
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id_descuento, tipo_descuento, valor, fecha_inicio, fecha_fin, estado_descuento, aplicacion
            FROM descuento
            WHERE id_descuento = %s
        """, (id_descuento,))
        descuento = cursor.fetchone()

    if not descuento:
        flash("Descuento no encontrado.", "danger")
        return redirect(url_for('descuento_bp.descuentos'))

    return render_template('Admin/actualizardescuento.html', descuento=descuento)