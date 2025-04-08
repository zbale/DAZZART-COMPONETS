# Importamos la función que nos permite conectar a la base de datos
from config.db import obtener_conexion

# Función para agregar un nuevo producto a la base de datos
def agregar_producto(nombre, descripcion, precio, stock, id_categoria, fecha_creacion):
    conexion = obtener_conexion()  # Abrimos conexión con la BD
    cursor = conexion.cursor()     # Creamos un cursor para ejecutar SQL
    sql = """
    INSERT INTO producto (nombre, descripcion, precio, stock, id_categoria, fecha_creacion)
    VALUES (%s, %s, %s, %s, %s, %s)
    """  # Consulta para insertar un nuevo producto
    # Ejecutamos la consulta pasando los valores recibidos
    cursor.execute(sql, (nombre, descripcion, precio, stock, id_categoria, fecha_creacion))
    conexion.commit()  # Guardamos los cambios en la base de datos
    cursor.close()     # Cerramos el cursor
    conexion.close()   # Cerramos la conexión

# Función para editar (actualizar) un producto existente
def editar_producto(id_producto, nombre, descripcion, precio, stock, id_categoria):
    conexion = obtener_conexion()  # Conectamos a la BD
    cursor = conexion.cursor()     # Creamos el cursor
    sql = """
    UPDATE producto SET nombre=%s, descripcion=%s, precio=%s, stock=%s, id_categoria=%s
    WHERE id_producto=%s
    """  # Consulta para actualizar los datos del producto con un ID específico
    # Ejecutamos la consulta con los nuevos valores
    cursor.execute(sql, (nombre, descripcion, precio, stock, id_categoria, id_producto))
    conexion.commit()  # Confirmamos los cambios
    cursor.close()     # Cerramos cursor
    conexion.close()   # Cerramos conexión

# Función para eliminar un producto según su ID
def eliminar_producto(id_producto):
    conexion = obtener_conexion()  # Conectamos a la BD
    cursor = conexion.cursor()     # Creamos cursor
    sql = "DELETE FROM producto WHERE id_producto=%"  # Consulta SQL para eliminar
    cursor.execute(sql, (id_producto,))  # Ejecutamos con el ID recibido
    conexion.commit()  # Confirmamos cambios
    cursor.close()     # Cerramos cursor
    conexion.close()   # Cerramos conexión

# Función para obtener todos los productos desde la base de datos
def obtener_productos():
    conexion = obtener_conexion()  # Conectamos a la BD
    cursor = conexion.cursor(dictionary=True)  # Usamos dictionary=True para obtener resultados como diccionarios
    cursor.execute("SELECT * FROM producto")   # Ejecutamos consulta para traer todos los productos
    productos = cursor.fetchall()              # Obtenemos todos los resultados
    cursor.close()     # Cerramos cursor
    conexion.close()   # Cerramos conexión
    return productos   # Retornamos los productos como una lista de diccionarios
