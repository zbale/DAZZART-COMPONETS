from flask import Blueprint, render_template, current_app
import pymysql

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin/pedidos')
def pedidos():
    connection = current_app.connection  # Usa current_app para acceder a la conexión
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Consulta SQL para obtener los pedidos
    cursor.execute("""
        SELECT 
            f.id_factura, 
            u.direccion, 
            u.nombre AS nombre_cliente, 
            GROUP_CONCAT(p.nombre SEPARATOR ', ') AS productos,
            SUM(df.cantidad) AS total_productos,
            SUM(p.precio * df.cantidad) AS total,
            f.estado
        FROM factura f
        JOIN usuario u ON f.id_usuario = u.id_usuario
        JOIN detalles_factura df ON f.id_factura = df.id_factura
        JOIN producto p ON df.id_producto = p.id_producto
        GROUP BY f.id_factura;
    """)

    resultados = cursor.fetchall()

    pedidos = []
    for fila in resultados:
        pedidos.append({
            'id_factura': fila['id_factura'],
            'direccion': fila['direccion'],
            'nombre_cliente': fila['nombre_cliente'],
            'productos': fila['productos'],
            'total_productos': fila['total_productos'],
            'total': float(fila['total']),
            'estado': fila['estado']
        })

    return render_template('admin/pedidos.html', pedidos=pedidos)

