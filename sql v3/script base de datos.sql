CREATE DATABASE IF NOT EXISTS DAZZART;
USE DAZZART;



CREATE TABLE usuario(
id_usuario INT auto_increment primary KEY,
nombre varchar(255) NOT NULL,
nombre_usuario varchar(255) NOT NULL,
correo_electronico varchar(255) NOT NULL,
telefono varchar (255) NOT NULL,
contrasena varchar(255) NOT NULL,
cedula varchar(255) NOT NULL,
direccion varchar(255) NOT NULL ,
rol ENUM('admin', 'cliente') NOT NULL
);


CREATE TABLE factura(
id_factura  INT auto_increment primary KEY,
Metodo_pago  varchar(255) NOT NULL,
fecha_factura DATE NOT NULL,
estado ENUM ('pagada', 'pendiente', 'cancelada') NOT NULL,
id_usuario INT,
FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE


);

CREATE TABLE categoria(
id_categoria  INT AUTO_INCREMENT PRIMARY KEY,
nombre_categoria varchar(255) NOT NULL,
descripcion_categoria varchar(255) NOT NULL
);

CREATE TABLE producto(
id_producto INT AUTO_INCREMENT PRIMARY KEY,
numero_serial varchar (30),
imagen varchar (255),
nombre VARCHAR(100) NOT NULL,
descripcion varchar(250) NOT NULL,
precio DECIMAL(10,2) NOT NULL,
stock INT NOT NULL,
id_categoria INT NOT NULL,
fecha_creacion DATE NOT NULL,
FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

CREATE TABLE detalles_factura(
id_detalle_factura INT AUTO_INCREMENT PRIMARY KEY,
cantidad  INT NOT NULL,
subtotal DECIMAL(10,2) NOT NULL,
id_factura INT NOT NULL,
id_producto INT NOT NULL,
FOREIGN KEY (id_factura) REFERENCES factura(id_factura) ON DELETE CASCADE,
FOREIGN KEY (id_producto) REFERENCES producto(id_producto) ON DELETE CASCADE
);



CREATE TABLE subcategoria(
id_subcategoria  INT AUTO_INCREMENT PRIMARY KEY,
nombre_subcategoria varchar(255),
descripcion_subcategoria varchar(255) NOT NULL,
id_categoria INT NOT NULL,
FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);
CREATE TABLE descuento (
    id_descuento INT AUTO_INCREMENT PRIMARY KEY,
    tipo_descuento ENUM('Porcentaje', 'Fijo') NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    estado_descuento ENUM('Activo', 'Inactivo') NOT NULL,
    aplicacion ENUM('producto', 'categoria') NOT NULL
);

-- Relación descuento-producto
CREATE TABLE descuento_producto (
    id_descuento INT NOT NULL,
    id_producto INT NOT NULL,
    PRIMARY KEY (id_descuento, id_producto),
    FOREIGN KEY (id_descuento) REFERENCES descuento(id_descuento) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto) ON DELETE CASCADE
);

-- Relación descuento-categoria
CREATE TABLE descuento_categoria (
    id_descuento INT NOT NULL,
    id_categoria INT NOT NULL,
    PRIMARY KEY (id_descuento, id_categoria),
    FOREIGN KEY (id_descuento) REFERENCES descuento(id_descuento) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria) ON DELETE CASCADE
);