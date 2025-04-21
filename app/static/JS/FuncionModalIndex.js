function actualizarCantidad(accion) {
    let cantidadInput = document.getElementById("cantidad");
    let cantidad = parseInt(cantidadInput.value);
    
    if (accion === "mas") {
        cantidad += 1;
    } else if (accion === "menos" && cantidad > 1) {
        cantidad -= 1;
    }
    
    cantidadInput.value = cantidad;
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("cantidad").addEventListener("input", function() {
        if (this.value < 1) {
            this.value = 1;
        }
    });
});