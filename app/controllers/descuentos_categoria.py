from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash, jsonify

descuento_categoria_bp = Blueprint('descuento_categoria_bp', __name__)

@descuento_categoria_bp.route('/admin/descuento_categoria', methods=['GET'])
def añadir_descuento_categoria():
    conn = current_app.connection
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria")
        categorias = cursor.fetchall()
        print("Categorías obtenidas:", categorias) 
    except Exception as e:
        print("Error al obtener categorías:", str(e))
        categorias = []
    
    return render_template('Admin/descuentocategoria.html', categorias=categorias)

@descuento_categoria_bp.route('/descuentocategoria', methods=['GET'])
def descuentos_categoria():
    conn = current_app.connection
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                d.id_descuento,
                c.nombre_categoria,
                d.porcentaje,
                d.estado_descuento
            FROM 
                descuento d
            JOIN 
                categoria c ON d.id_categoria = c.id_categoria
            WHERE 
                d.tipo_descuento = 'Categoria'
        """)
        descuentos = cursor.fetchall()
    except Exception as e:
        print("Error al obtener descuentos:", str(e))
        descuentos = []
    
    return render_template('Admin/descuentocategoria.html', descuentos=descuentos)


@descuento_categoria_bp.route('/descuentocategoria/agregar', methods=['GET', 'POST'])
def agregar_descuento_categoria():
    conn = current_app.connection
    cursor = conn.cursor()

    if request.method == 'POST':

        categoria_id = request.form['id_categoria']
        tipo_descuento = 'Categoria'
        valor_descuento = request.form['porcentaje']
        estado = request.form['estado']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']

        try:
            cursor.execute("""
                INSERT INTO descuento (id_categoria, tipo_descuento, porcentaje, estado_descuento, fecha_inicio, fecha_fin)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (categoria_id, tipo_descuento, valor_descuento, estado, fecha_inicio, fecha_fin))
            conn.commit()
            flash("Descuento agregado correctamente", "success")
        except Exception as e:
            print("Error al agregar descuento:", str(e))
            flash("Error al agregar descuento", "danger")
        return redirect(url_for('descuento_categoria_bp.descuentos_categoria'))
    else:
        cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria")
        categorias = cursor.fetchall()
        return render_template('Admin/actualizardescuentocategorias.html', categorias=categorias)

@descuento_categoria_bp.route('/descuentocategoria/editar/<int:id>', methods=['POST'])
def editar_descuento_categoria(id):
    nuevo_porcentaje = request.form['porcentaje']
    nuevo_estado = request.form.get('estado', 1)

    conn = current_app.connection
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE descuento
                SET porcentaje = %s, estado_descuento = %s
                WHERE id_descuento = %s
            """, (nuevo_porcentaje, nuevo_estado, id))
            conn.commit()
        flash("Descuento actualizado", "info")
    except Exception as e:
        print("Error al actualizar descuento:", str(e))
        flash("Error al actualizar el descuento", "danger")
    
    return redirect(url_for('descuento_categoria_bp.descuentos_categoria'))


@descuento_categoria_bp.route('/descuentocategoria/eliminar/<int:id>', methods=['POST'])
def eliminar_descuento_categoria(id):
    conn = current_app.connection
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM descuento WHERE id_descuento = %s", (id,))
            conn.commit()
        flash("Descuento eliminado", "danger")
    except Exception as e:
        print("Error al eliminar descuento:", str(e))
        flash("Error al eliminar el descuento", "danger")
    
    return redirect(url_for('descuento_categoria_bp.descuentos_categoria'))


@descuento_categoria_bp.route('/descuentocategoria/editar_estado/<int:id>', methods=['POST'])
def editar_estado_descuento(id):
    data = request.get_json()  
    nuevo_estado = data['estado'] 

    conn = current_app.connection
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE descuento
                SET estado_descuento = %s
                WHERE id_descuento = %s
            """, (nuevo_estado, id))
            conn.commit()
        return jsonify({"message": "Estado actualizado correctamente"}), 200
    except Exception as e:
        print("Error al actualizar estado del descuento:", str(e))
        return jsonify({"error": "No se pudo actualizar el estado"}), 500
