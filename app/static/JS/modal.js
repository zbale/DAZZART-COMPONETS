document.addEventListener("DOMContentLoaded", function () {
    // aqui es para que muestre el modal cuando se haga clic en el icono de login
    document.getElementById("login-btn").addEventListener("click", function () {
        var myModal = new bootstrap.Modal(document.getElementById("login-modal"));
        myModal.show();
    });
});