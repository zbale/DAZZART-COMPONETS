from flask import Blueprint, render_template, current_app
import pymysql

admin_bp = Blueprint('admin_bp', __name__)

# Ruta para ver todos los pedidos
@admin_bp.route('/pedidos')
def pedidos():
    connection = current_app.connection  
    cursor = connection.cursor(pymysql.cursors.DictCursor)

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

    return render_template('Admin/pedidos.html', pedidos=pedidos)

# Ruta para ver el detalle de una factura
@admin_bp.route('/pedidos/<int:id_factura>')
def ver_factura(id_factura):
    connection = current_app.connection
    cursor = connection.cursor(pymysql.cursors.DictCursor)

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
        WHERE f.id_factura = %s
        GROUP BY f.id_factura;
    """, (id_factura,))

    factura = cursor.fetchone()

    if not factura:
        return "Factura no encontrada", 404

    return render_template('Admin/factura.html', factura=factura)

