cursor = conexion.cursor()
#insertar producto
sql = "INSERT INTO producto (nombre, precio, stock) VALUES (%s, %s, %s)"
valores = ("Producto Prueba", 19900, 5)
cursor.execute(sql, valores)
conexion.commit()

print("Producto insertado correctamente")
cursor.close()
conexion.close()
