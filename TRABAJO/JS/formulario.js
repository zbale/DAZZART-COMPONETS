(() => {
    'use strict';

    // mostrar/ocultar (rol)
    function toggleAdminKey() {
        let rol = document.getElementById("rol").value;
        let adminKeyContainer = document.getElementById("adminKeyContainer");
        let adminKeyInput = document.getElementById("adminKey");

        if (rol === "admin") {
            adminKeyContainer.style.display = "block";
            adminKeyInput.setAttribute("required", "true");
        } else {
            adminKeyContainer.style.display = "none";
            adminKeyInput.removeAttribute("required");
            adminKeyInput.value = "";
        }
    }

    document.addEventListener("DOMContentLoaded", function () {
        toggleAdminKey(); 
        document.getElementById("rol").addEventListener("change", toggleAdminKey);
    });

    
    document.querySelector(".needs-validation").addEventListener("submit", function (event) {
        let form = event.target;
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }

        let rol = document.getElementById("rol").value;
        let adminKeyInput = document.getElementById("adminKey");
        const superAdminKey = "1234";

        // Validar clave 
        if (rol === "admin") {
            if (adminKeyInput.value.trim() === "") {
                adminKeyInput.classList.add("is-invalid");
                event.preventDefault();
                event.stopPropagation();
            } else {
                adminKeyInput.classList.remove("is-invalid");
                if (adminKeyInput.value !== superAdminKey) {
                    event.preventDefault();
                    alert("Clave de administrador incorrecta.");
                }
            }
        }

        form.classList.add("was-validated");
    }, false);
})();
