document.querySelector('.btn-ingresar').addEventListener("click", function(event) {
    event.preventDefault(); 

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    if (email === '' || password === '') {
        Swal.fire({
            icon: "warning",
            title: "Campos vacíos",
            text: "Por favor, completa todos los campos antes de continuar.",
            confirmButtonText: "Aceptar",
        });
        return;
    }

    // Simulamos una base de datos en un objeto JS
    const usuarios = [
        { email: "admin@valecita.com", password: "2024", rol: "admin" },
        { email: "josedaviddazacamacho@gmail.com", password: "2024", rol: "usuario" }
    ];

    // Buscar el usuario en la "base de datos simulada"
    const usuario = usuarios.find(user => user.email === email && user.password === password);

    if (usuario) {
        Swal.fire({
            icon: "success",
            title: "Inicio Exitoso!",
            text: usuario.rol === "admin" ? "Bienvenido Administrador." : "Bienvenido Usuario.",
            confirmButtonText: "Ingresar",
        }).then(() => {
            if (usuario.rol === "admin") {
                window.location.href = 'Administrador/';
            } else {
                window.location.href = 'categorias.html';
            }
        });
    } else {
        Swal.fire({
            icon: "error",
            title: "Credenciales Incorrectas",
            text: "El correo o la contraseña no son válidos.",
            confirmButtonText: "Intentar de nuevo",
        });
    }
});
