#vamos a definir la lógica para el registro, login y perfil, utilizando consultas SQL manuales. Este código se conecta directamente a la base de datos y ejecuta consultas SQL para el login, registro, y el perfil de usuario.
from flask import Blueprint, render_template, request, redirect, url_for, current_app
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
                       return render_template('Admin/gestionUs.html')  
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
