document.addEventListener("DOMContentLoaded", function () {
    // aqui es para que muestre el modal cuando se haga clic en el icono de login
    document.getElementById("login-btn").addEventListener("click", function () {
        var myModal = new bootstrap.Modal(document.getElementById("login-modal"));
        myModal.show();
    });

    // el manejo del formulario de login
    document.querySelector("form").addEventListener("submit", function (event) {
        event.preventDefault(); 

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();



        // aqui se verifica si los campos están vacíos
        if (email === "" || password === "") {
            Swal.fire({
                icon: "warning",
                title: "Campos vacíos",
                text: "Por favor, completa todos los campos antes de continuar.",
                confirmButtonText: "Aceptar",
            });
            return;
        }

        const usuarios = {
            "admin@valecita.com": "2024",
            "josedaviddazacamacho@gmail.com": "2024",
        };

        // se valida si el usuario y la contraseña son correctos
        if (usuarios[email] && usuarios[email] === password) {
            Swal.fire({
                icon: "success",
                title: "Inicio Exitoso!",
                text: email === "admin@valecita.com" ? "Bienvenido Administrador." : "Bienvenido!",
                confirmButtonText: "Ingresar",
            }).then(() => {
                window.location.href = "ADMIN/categorias.html";
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
});
