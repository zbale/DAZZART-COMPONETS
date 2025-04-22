USE DAZZART;
/*mostrar detalles de la orden*/
SELECT 
    p.nombre AS nombreproducto, 
    p.precio
FROM producto p
JOIN detalles_factura df ON p.id_producto = df.id_producto;
-- Listar todos los usuarios y sus facturas (incluso si no han comprado nada) -- 
SELECT usuario.nombre, factura.id_factura, factura.estado 
FROM usuario
LEFT JOIN factura ON usuario.id_usuario = factura.id_usuario;
-- Seleccionar todos los productos con sus categorías y subcategorías (si las tienen)
SELECT 
    producto.id_producto,
    producto.nombre AS nombre_producto,
    categoria.nombre_categoria,
    subcategoria.nombre_subcategoria
FROM 
    producto
LEFT JOIN 
    categoria ON producto.id_categoria = categoria.id_categoria
LEFT JOIN 
    subcategoria ON categoria.id_categoria = subcategoria.id_categoria;

   /*mostrar los productos, descripciones, precio, cantidad y categoria*/
SELECT 
    p.nombre AS producto,
    p.descripcion AS descripcion,
    p.precio,
    p.stock AS cantidad,
    c.nombre_categoria AS categoria
FROM producto p
JOIN categoria c ON p.id_categoria = c.id_categoria;

-- Listar categorías y los productos asociados (incluyendo categorías sin productos)--
SELECT categoria.nombre_categoria, producto.nombre 
FROM categoria
LEFT JOIN producto ON categoria.id_categoria = producto.id_categoria;    
-- obtener subcategorias  y sus categorias
SELECT s.id_subcategoria, s.nombre_subcategoria, s.descripcion_subcategoria,
c.id_categoria, c.nombre_categoria
FROM subcategoria s
JOIN categoria c ON s.id_categoria = c.id_categoria
    