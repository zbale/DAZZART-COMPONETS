@user_bp.route('/crear-subcategoria', methods=['GET', 'POST'])

def crear_subcategoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        id_categoria = request.form['id_categoria']

        connection = current_app.connection
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO subcategoria (nombre_subcategoria, descripcion_subcategoria, id_categoria) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, descripcion, id_categoria))
                connection.commit()
                  return render_template('Admin/añadirsubcategoria.html')
        except Exception as e:
            return str(e)

    return render_template('Admin/añadirsubcategoria.html')
