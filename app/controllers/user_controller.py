#vamos a definir la lógica para el registro, login y perfil, utilizando consultas SQL manuales. Este código se conecta directamente a la base de datos y ejecuta consultas SQL para el login, registro, y el perfil de usuario.
from flask import Blueprint, render_template, request, redirect, url_for, current_app,flash
from flask_bcrypt import Bcrypt
from flask import session

user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  
        password = request.form['password']

        connection = current_app.connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT contrasena, rol FROM usuario WHERE correo_electronico=%s", (email,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result['contrasena'], password):
                    session['user_email'] = email
                    session['user_rol'] = result['rol']  # Guardamos el rol también

                    if result['rol'] == 'admin':
                        return redirect(url_for('user_bp.listar_usuarios'))
                    else:
                        return render_template('Cliente/index.html')
                else:
                    return "Login Failed"
        except Exception as e:
            return str(e)

    return render_template('Cliente/index.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    connection = current_app.connection
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombre_usuario = request.form['nombre_usuario']
        correo = request.form['correo_electronico']
        telefono = request.form['telefono']
        cedula = request.form['cedula']
        direccion = request.form['direccion']
        password = request.form['contrasena']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        rol = 'cliente'  

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO usuario (nombre, nombre_usuario, correo_electronico, telefono, contrasena, cedula, direccion, rol)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (nombre, nombre_usuario, correo, telefono, hashed_password, cedula, direccion, rol))
                connection.commit()
            return redirect(url_for('user_bp.login'))
        except Exception as e:
            return str(e)

    return render_template('Cliente/registro.html') 

@user_bp.route('/profile')
def profile():
    email = session.get('user_email')
    if not email:
        return redirect(url_for('user_bp.login'))
    
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT nombre, nombre_usuario, correo_electronico, telefono, cedula, direccion, rol FROM usuario WHERE correo_electronico=%s", (email,))
            user = cursor.fetchone()
            if not user:
                return "Usuario no encontrado"
    except Exception as e:
        return str(e)

    return render_template('profile.html', user=user)

@user_bp.route('/admin/usuarios')
def listar_usuarios():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE rol != 'admin'")
            usuarios = cursor.fetchall()
    except Exception as e:
        return str(e)

    return render_template('Admin/gestionUs.html', usuarios=usuarios)
@user_bp.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        nombre_usuario = request.form['nombre_usuario']
        correo = request.form['correo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        contrasena = request.form['contrasena']
        rol = request.form['rol']

        # Encriptar contraseña con Flask-Bcrypt
        hashed_password = bcrypt.generate_password_hash(contrasena).decode('utf-8')

        connection = current_app.connection  # 💡 Este es el que debes usar
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO usuario 
                    (cedula, nombre, nombre_usuario, correo_electronico, telefono, direccion, contrasena, rol) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (cedula, nombre, nombre_usuario, correo, telefono, direccion, hashed_password, rol))
                connection.commit()
                print("Usuario agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            connection.rollback()

        return redirect(url_for('user_bp.listar_usuarios'))

    return render_template('Admin/añadirusuario.html')
@user_bp.route('/usuarios/eliminar/<int:id_usuario>', methods=['POST'])
def eliminar_usuario(id_usuario):
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
            connection.commit()
            flash('Usuario eliminado correctamente', 'success')
    except Exception as e:
        print("Error al eliminar usuario:", e)
        flash('Error al eliminar usuario', 'danger')
    
    return redirect(url_for('user_bp.listar_usuarios'))


@user_bp.route('/usuarios/editar/<int:id_usuario>', methods=['GET'])
def editar_usuario(id_usuario):
    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
        usuario = cursor.fetchone()
    return render_template('Admin/actualizarusuario.html', usuario=usuario)

@user_bp.route('/usuarios/editar/<int:id_usuario>', methods=['POST'])
def actualizar_usuario(id_usuario):
    nombre = request.form['nombre']
    nombre_usuario = request.form['nombre_usuario']
    correo = request.form['correo']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    rol = request.form['rol']
    contrasena = request.form['contrasena']

    query = """
        UPDATE usuario SET
            nombre=%s,
            nombre_usuario=%s,
            correo_electronico=%s,
            telefono=%s,
            direccion=%s,
            rol=%s
        WHERE id_usuario=%s
    """
    params = (nombre, nombre_usuario, correo, telefono, direccion, rol, id_usuario)

    connection = current_app.connection
    with connection.cursor() as cursor:
        cursor.execute(query, params)

        # Si el campo de contraseña no está vacío, actualizamos aparte usando bcrypt
        if contrasena.strip():
            from flask_bcrypt import Bcrypt
            bcrypt = Bcrypt(current_app)  # importante si no lo estás usando como extensión global
            hashed_password = bcrypt.generate_password_hash(contrasena).decode('utf-8')
            cursor.execute("UPDATE usuario SET contrasena=%s WHERE id_usuario=%s", (hashed_password, id_usuario))

        connection.commit()

    return redirect(url_for('user_bp.listar_usuarios'))


@user_bp.route("/compras")
def compras():
    return render_template("Cliente/compras.html")

@user_bp.route("/detallefactura")
def detallefactura():
    return render_template("Cliente/Detallesfactura.html")

@user_bp.route("/producto")
def producto():
    return render_template("Cliente/producto.html")

@user_bp.route("/interfazpro")
def interfazpro():
    return render_template("Cliente/interfazproductos.html")