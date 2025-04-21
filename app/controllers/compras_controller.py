from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from datetime import datetime

compras_bp = Blueprint('compras', __name__)

@compras_bp.route('/compras', methods=['GET'])
def mostrar_compras():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_producto, nombre_producto, precio FROM producto")
            productos = cursor.fetchall()

        carrito = [
            {'id': p['id_producto'], 'nombre': p['nombre_producto'], 'precio': p['precio'], 'cantidad': 1}
            for p in productos
        ]
        total = sum(p['precio'] * p['cantidad'] for p in carrito)

        return render_template('Index/compras.html', carrito=carrito, total=total)
    except Exception as e:
        print("Error al cargar compras:", e)
        return render_template('Index/compras.html', carrito=[], total=0)

@compras_bp.route('/detallesfactura', methods=['GET'])
def detalles_factura():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            hoy = datetime.now().strftime('%Y-%m-%d')

            query = """
                SELECT 
                    p.id_producto,
                    p.nombre_producto,
                    p.precio,
                    c.id_categoria,
                    d.tipo_descuento,
                    d.porcentaje,
                    d.estado_descuento,
                    d.fecha_inicio,
                    d.fecha_fin
                FROM producto p
                LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
                LEFT JOIN descuento d ON (
                    (d.tipo_descuento = 'Producto' AND d.id_producto = p.id_producto)
                    OR 
                    (d.tipo_descuento = 'Categoria' AND d.id_categoria = c.id_categoria)
                )
                WHERE 
                    (d.estado_descuento = 'Activo' AND %s BETWEEN d.fecha_inicio AND d.fecha_fin)
                    OR d.id_descuento IS NULL;
            """
            cursor.execute(query, (hoy,))
            productos = cursor.fetchall()

        carrito = []
        for p in productos:
            precio_original = p['precio']
            descuento = p['porcentaje']

            if descuento:
                precio_final = round(precio_original * (1 - descuento / 100), 2)
            else:
                precio_final = precio_original

            carrito.append({
                'id': p['id_producto'],
                'nombre': p['nombre_producto'],
                'precio_original': precio_original,
                'descuento': descuento,
                'precio_final': precio_final,
                'cantidad': 1
            })

        subtotal = sum(p['precio_original'] * p['cantidad'] for p in carrito)
        total = sum(p['precio_final'] * p['cantidad'] for p in carrito)
        descuento_total = subtotal - total
        porcentaje_descuento = round((descuento_total / subtotal) * 100) if subtotal else 0

        return render_template(
            'Index/Detallesfactura.html',
            carrito=carrito,
            subtotal=subtotal,
            descuento=porcentaje_descuento,
            total=total
        )

    except Exception as e:
        print("Error al aplicar descuento:", e)
        return render_template('Index/Detallesfactura.html', carrito=[], subtotal=0, descuento=0, total=0)