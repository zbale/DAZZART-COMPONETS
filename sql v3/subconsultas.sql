-- Obtener facturas que tengan más de 2 productos diferentes
SELECT f.id_factura, f.fecha_factura
FROM factura f
WHERE (
    SELECT COUNT(DISTINCT id_producto) 
    FROM detalles_factura df 
    WHERE df.id_factura = f.id_factura
) > 2;

-- Productos sin stock 
SELECT nombre, stock
FROM producto
WHERE id_producto IN (
    SELECT id_producto
    FROM producto
    WHERE stock = 0
);