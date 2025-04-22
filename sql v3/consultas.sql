USE DAZZART;
-- listar todos los usuario --
SELECT * FROM usuario;

-- visualizar los nombres de las personas registradas en el ecommerce --
select nombre_cliente from usuario;
-- actualizar la direccion de un usuario--
UPDATE usuario  SET direccion = 'calle 98' where id_usuario = 8;

-- actualizar el stock de un producto --
UPDATE producto SET stock = stock - 1 where id_producto = 9;

-- añadir un nuevo producto--
INSERT INTO producto (nombre, descripcion, precio, stock, id_categoria, fecha_creacion) VALUES
('coleer memo dl06 ', 'disipador para telefono inteligente', 50.00, 11, 8, '2025-04-14');

-- consultar categoria en especifico --
select nombre_categoria AS categoria from categoria WHERE  nombre_categoria = 'Monitores';

-- visualizar el estado del pago de un producto y sus datos--
select * from factura where estado = 'pagada';

-- counsultar los datos de una compra realizada en un mes en especifico --
SELECT * FROM factura WHERE fecha_factura = '2025-03-07';
-- buscar los productos con un precio mayor o igual a un precio--
SELECT nombre AS producto , precio from producto where precio >= 89.99;
-- actualizar un descuneto aplicado --
UPDATE descuento
SET tipo_descuento = 'Producto',
    valor = 15.00,
    fecha_inicio = '2025-05-01',
    fecha_fin = '2025-05-31',
    estado_descuento = 'Activo'
WHERE id_descuento = 1;
