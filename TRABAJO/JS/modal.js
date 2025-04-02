document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector("#login-modal form");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita que el formulario se envíe automáticamente

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (email === "" || password === "") {
            mostrarAlerta("Por favor, completa todos los campos.");
            return;
        }

        // Aquí puedes agregar más validaciones o lógica para autenticar al usuario
        console.log("Usuario:", email);
        console.log("Contraseña:", password);
    });
});

function mostrarAlerta(mensaje) {
    const alerta = document.createElement("div");
    alerta.className = "alert alert-warning position-fixed top-0 start-50 translate-middle-x mt-3";
    alerta.style.zIndex = "1050";
    alerta.textContent = mensaje;

    document.body.appendChild(alerta);

    setTimeout(() => {
        alerta.remove();
    }, 3000);
}





