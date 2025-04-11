USE DAZZART;

INSERT INTO usuario (id_usuario,nombre, nombre_usuario, correo_electronico,telefono,contrasena,cedula, direccion,rol) VALUES
(1,'Jose David Daza Camacho', 'jose131', 'josecrack13113@gmail.com', '3143688476', '$2b$12$pO/kZYWpAs6HD5sUnoaGPeGlDf5G4vJTEoTpIy9a8UbsUdv9jw.Nq','1001201759', 'tv 110a #80a-80', 'admin'); 

SELECT * FROM usuario;

INSERT INTO factura (Metodo_pago, fecha_factura, estado, id_usuario) VALUES
('Tarjeta de Crédito', '2025-03-01', 'pagada', 1),
('PayPal', '2025-03-02', 'pendiente', 2),
('Transferencia Bancaria', '2025-03-03', 'cancelada', 3),
('Efectivo', '2025-03-04', 'pagada', 4),
('Tarjeta de Débito', '2025-03-05', 'pendiente', 5),
('PayPal', '2025-03-06', 'pagada', 6),
('Efectivo', '2025-03-07', 'cancelada', 7),
('Transferencia Bancaria', '2025-03-08', 'pendiente', 8),
('Tarjeta de Crédito', '2025-03-09', 'pagada', 9),
('Efectivo', '2025-03-10', 'cancelada', 10),
('Efectivo', '2025-06-10', 'cancelada', 10);


SELECT * FROM factura;


INSERT INTO categoria (nombre_categoria, descripcion_categoria) VALUES
('Computadoras', 'Equipos de cómputo y accesorios'),
('Periféricos', 'Dispositivos externos como teclados y ratones'),
('Componentes de Hardware', 'Partes internas de una PC'),
('Sillas Gamer', 'Sillas ergonómicas para gaming'),
('Accesorios', 'Fundas, soportes y cables para PC'),
('Software', 'Licencias de software y antivirus'),
('Redes', 'Equipos para conexión a Internet'),
('Impresoras', 'Dispositivos de impresión y escaneo'),
('Almacenamiento', 'Discos duros y unidades flash'),
('Monitores', 'Pantallas para computadoras de alta resolución');


SELECT * FROM categoria;

INSERT INTO subcategoria (nombre_subcategoria, descripcion_subcategoria, id_categoria) VALUES
('Laptops', 'Computadoras portátiles', 1),
('PCs de Escritorio', 'Computadoras de alto rendimiento', 1),
('Teclados', 'Teclados mecánicos y ergonómicos', 2),
('Ratones', 'Ratones ópticos y láser', 2),
('Memoria RAM', 'Módulos de memoria de alto rendimiento', 3),
('Procesadores', 'CPUs de última generación', 3),
('Sillas ergonómicas', 'Sillas con ajuste lumbar y reclinables', 4),
('Cables HDMI', 'Cables para transmisión de video', 5),
('Antivirus', 'Software de seguridad informática', 6),
('Routers WiFi', 'Dispositivos de conexión inalámbrica', 7);
SELECT * FROM subcategoria;

INSERT INTO producto (numero_serial, imagen, nombre, descripcion, precio, stock, id_categoria, fecha_creacion) VALUES
('NS-001', 'IMG/default.png', 'Laptop HP Envy', 'Ultrabook con pantalla táctil', 1199.99, 15, 1, '2025-03-05'),
('NS-002', 'IMG/default.png', 'PC Gamer Alienware', 'Computadora con RTX 4080', 2999.99, 8, 1, '2025-03-06'),
('NS-003', 'IMG/default.png', 'Teclado Mecánico Razer', 'Teclado RGB con switches ópticos', 149.99, 25, 2, '2025-03-07'),
('NS-004', 'IMG/default.png', 'Mouse Logitech G502', 'Ratón gaming de alta precisión', 89.99, 40, 2, '2025-03-08'),
('NS-005', 'IMG/default.png', 'Memoria RAM Kingston 32GB', 'DDR5 para alto rendimiento', 199.99, 30, 3, '2025-03-09'),
('NS-006', 'IMG/default.png', 'Procesador AMD Ryzen 9', 'CPU de alto rendimiento', 499.99, 10, 3, '2025-03-10'),
('NS-007', 'IMG/default.png', 'Silla Gamer Corsair', 'Silla ergonómica con ajuste lumbar', 249.99, 20, 4, '2025-03-11'),
('NS-008', 'IMG/default.png', 'Cable HDMI 2.1', 'Cable de ultra alta velocidad', 29.99, 50, 5, '2025-03-12'),
('NS-009', 'IMG/default.png', 'Antivirus Norton', 'Protección completa para PC', 79.99, 35, 6, '2025-03-13'),
('NS-010', 'IMG/default.png', 'Router TP-Link AX6000', 'WiFi 6 para conexiones rápidas', 179.99, 15, 7, '2025-03-14');


 SELECT * FROM producto;
INSERT INTO detalles_factura (cantidad, subtotal, id_factura, id_producto) VALUES
(1, 1199.99, 1, 1),
(1, 2999.99, 2, 2),
(2, 299.98, 3, 3),
(1, 89.99, 4, 4),
(2, 399.98, 5, 5),
(1, 499.99, 6, 6),
(1, 249.99, 7, 7),
(3, 89.97, 8, 8),
(1, 79.99, 9, 9),
(2, 359.98, 10, 10);
 SELECT * FROM detalles_factura;
INSERT INTO descuento (tipo_descuento, porcentaje, estado_descuento, id_producto, id_categoria) VALUES
('Producto', 10.00, 'Activo', 1, NULL),
('Producto', 15.00, 'Activo', 2, NULL),
('Producto', 5.00, 'Activo', 3, NULL),
('Producto', 8.00, 'Activo', 4, NULL),
('Producto', 12.00, 'Activo', 5, NULL),
('Producto', 20.00, 'Activo', 6, NULL),
('Producto', 10.00, 'Activo', 7, NULL),
('Producto', 25.00, 'Activo', 8, NULL),
('Producto', 15.00, 'Activo', 9, NULL),
('Categoria', 10.00, 'Activo', NULL, 1);  

 SELECT * FROM descuento;