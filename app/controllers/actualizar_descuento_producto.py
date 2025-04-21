from flask import Blueprint, render_template, current_app, flash, redirect, url_for, request

# Definición del Blueprint
descuentos_bp = Blueprint('descuentos', __name__)

# Ruta para listar descuentos (CRUD principal) - Descuentos por Producto
@descuentos_bp.route('/descuento_producto', methods=['GET'])
def listar_descuentos_producto():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            query_descuentos = """
                SELECT 
                    d.id_descuento,
                    p.nombre AS nombre_producto,
                    p.precio AS precio_original,
                    d.porcentaje AS porcentaje_descuento,
                    (p.precio - (p.precio * d.porcentaje / 100)) AS precio_con_descuento,
                    d.estado_descuento,
                    d.fecha_inicio,
                    d.fecha_fin
                FROM 
                    descuento d
                JOIN 
                    producto p ON d.id_producto = p.id_producto
                WHERE 
                    d.tipo_descuento = 'Producto';
            """
            cursor.execute(query_descuentos)
            lista_descuentos = cursor.fetchall()
            print("Descuentos obtenidos:", lista_descuentos)
        return render_template('Admin/actualizardescpro.html', lista_descuentos=lista_descuentos)
    except Exception as e:
        print("Error al obtener datos:", e)
        return render_template('Admin/actualizardescpro.html', lista_descuentos=[])

# Ruta para mostrar el formulario para añadir descuentos - Descuentos por Producto
@descuentos_bp.route('/descuento_producto/agregar', methods=['GET', 'POST'])
def mostrar_formulario_descuento():
    connection = current_app.connection

    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_producto, nombre FROM producto")
                productos = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            productos = []

        return render_template('Admin/añadirdescuentoprod.html', productos=productos)

    elif request.method == 'POST':
        # Obtener datos del formulario
        id_producto = request.form.get('id_producto')  # ID del producto seleccionado
        porcentaje = request.form.get('porcentaje')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        estado_descuento = request.form.get('estado_descuento')

        # Depuración: Verificar los datos recibidos
        print("Datos recibidos del formulario:")
        print("ID Producto:", id_producto)
        print("Porcentaje:", porcentaje)
        print("Fecha Inicio:", fecha_inicio)
        print("Fecha Fin:", fecha_fin)
        print("Estado:", estado_descuento)

        # Verificar que todos los campos necesarios estén presentes
        if not id_producto or not porcentaje or not fecha_inicio or not fecha_fin or not estado_descuento:
            flash('Todos los campos son obligatorios.', 'danger')
            return redirect(url_for('descuentos.mostrar_formulario_descuento'))

        try:
            # Insertar descuento en la base de datos
            with connection.cursor() as cursor:
                query = """
                    INSERT INTO descuento (porcentaje, id_producto, tipo_descuento, fecha_inicio, fecha_fin, estado_descuento)
                    VALUES (%s, %s, 'Producto', %s, %s, %s);
                """
                cursor.execute(query, (porcentaje, id_producto, fecha_inicio, fecha_fin, estado_descuento))
                connection.commit()

            flash('Descuento agregado exitosamente.', 'success')
        except Exception as e:
            print("Error al agregar descuento:", e)
            flash('Error al agregar el descuento.', 'danger')

        # Redirigir al listado de descuentos una vez se haya agregado el descuento
        return redirect(url_for('descuentos.listar_descuentos_producto'))


# Ruta para eliminar un descuento - Descuentos por Producto
@descuentos_bp.route('/descuento_producto/eliminar/<int:id>', methods=['POST'])
def eliminar_descuento_producto(id):
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            query = "DELETE FROM descuento WHERE id_descuento = %s"
            cursor.execute(query, (id,))
            connection.commit()
            flash('Descuento eliminado exitosamente.', 'success')
    except Exception as e:
        print("Error al eliminar descuento:", e)
        flash('Error al eliminar el descuento.', 'danger')

    return redirect(url_for('descuentos.listar_descuentos_producto'))

# Ruta para agregar un descuento - Descuentos por Producto
@descuentos_bp.route('/descuento_producto/agregar', methods=['POST'])
def agregar_descuento_producto():
    connection = current_app.connection
    if request.method == 'POST':
        # Obtener datos del formulario
        id_producto = request.form.get('id_producto')  # ID del producto seleccionado
        porcentaje = request.form.get('porcentaje')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        estado_descuento = request.form.get('estado_descuento')

        # Depuración: Verificar los datos recibidos
        print("Datos recibidos del formulario:")
        print("ID Producto:", id_producto)
        print("Porcentaje:", porcentaje)
        print("Fecha Inicio:", fecha_inicio)
        print("Fecha Fin:", fecha_fin)
        print("Estado:", estado_descuento)

        # Verificar que todos los campos necesarios estén presentes
        if not id_producto or not porcentaje or not fecha_inicio or not fecha_fin or not estado_descuento:
            flash('Todos los campos son obligatorios.', 'danger')
            return redirect(url_for('descuentos.mostrar_formulario_descuento'))

        try:
            # Insertar descuento en la base de datos
            with connection.cursor() as cursor:
                query = """
                    INSERT INTO descuento (porcentaje, id_producto, tipo_descuento, fecha_inicio, fecha_fin, estado_descuento)
                    VALUES (%s, %s, 'Producto', %s, %s, %s);
                """
                cursor.execute(query, (porcentaje, id_producto, fecha_inicio, fecha_fin, estado_descuento))
                connection.commit()

            flash('Descuento agregado exitosamente.', 'success')
        except Exception as e:
            print("Error al agregar descuento:", e)
            flash('Error al agregar el descuento.', 'danger')

        # Redirigir al listado de descuentos una vez se haya agregado el descuento
        return redirect(url_for('descuentos.listar_descuentos_producto'))

# Ruta para editar un descuento - Descuentos por Producto
@descuentos_bp.route('/descuento_producto/editar/<int:id>', methods=['GET', 'POST'])
def editar_descuento_producto(id):
    connection = current_app.connection
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM descuento WHERE id_descuento = %s", (id,))
                descuento = cursor.fetchone()
            return render_template('Admin/editar_descuentoprod.html', descuento=descuento)
        except Exception as e:
            print("Error al obtener descuento:", e)
            flash('Error al cargar el descuento.', 'danger')
            return redirect(url_for('descuentos.listar_descuentos_producto'))
    elif request.method == 'POST':
        pass




