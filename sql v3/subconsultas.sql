/*Obtener productos con descuentos mayores al 20% (si son de tipo porcentaje)*/
SELECT * 
FROM producto 
WHERE id_producto IN (
    SELECT id_producto 
    FROM descuento_producto dp
    JOIN descuento d ON dp.id_descuento = d.id_descuento
    WHERE d.tipo_descuento = 'Porcentaje' AND d.valor > 20
);
 /*Nombre de usuarios que tienen facturas pendientes*/
 SELECT nombre
FROM usuario 
WHERE id_usuario IN (
    SELECT id_usuario 
    FROM factura 
    WHERE estado = 'pendiente'
);
/*Productos con descuento activo*/
SELECT * 
FROM producto 
WHERE id_producto IN (
    SELECT id_producto 
    FROM descuento_producto dp
    JOIN descuento d ON dp.id_descuento = d.id_descuento
    WHERE d.estado_descuento = 'Activo'
);


/*Productos con descuento inactivo*/
SELECT * 
FROM producto 
WHERE id_producto IN (
    SELECT id_producto 
    FROM descuento_producto dp
    JOIN descuento d ON dp.id_descuento = d.id_descuento
    WHERE d.estado_descuento = 'inactivo'
);
