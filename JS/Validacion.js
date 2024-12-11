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


    if (email === "admin@valecita.com" && password === "2024") {
        Swal.fire({
            icon: "success",
            title: "Inicio Exitoso!",
            text: "Bienvenido Administrador.",
            confirmButtonText: "Ingresar",
        }).then(() => {
            window.location.href = 'Administrador/';
        });
        return;
    } 
    
    else if (email === "josedaviddazacamacho@gmail.com" && password === "2024") {
            Swal.fire({
                icon: "success",
                title: "Inicio Exitoso!",
                confirmButtonText: "Ingresar",
            }).then(() => {
                window.location.href = 'categorias.html';
            });
            return;
        }
    
    
    
    else {
        Swal.fire({
            icon: "error",
            title: "Credenciales Incorrectas",
            text: "El correo o la contraseña no son válidos.",
            confirmButtonText: "Intentar de nuevo",
        });
    }
});