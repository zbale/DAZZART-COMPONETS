function abrirMenu() {
    const menu = document.querySelector('.menu-lateral');
    menu.classList.toggle('activo');
}

function cerrarMenu() {
    const menu = document.querySelector('.menu-lateral');
    menu.classList.remove('activo'); // Elimina la clase para cerrar el menú
}

// Carousel (Ya incluido en tu código)
let currentIndex = 0;
const images = document.querySelector('.carousel-images');
const totalImages = document.querySelectorAll('.carousel-images img').length;

function moveSlide(direction) {
    currentIndex += direction;
    if (currentIndex >= totalImages) {
        currentIndex = 0; 
    } else if (currentIndex < 0) {
        currentIndex = totalImages - 1; 
    }
    images.style.transform = `translateX(-${currentIndex * 33.33}%)`;
}

setInterval(() => {
    moveSlide(1); 
}, 3200);



function cambiarCantidad(incremento) {
    const cantidadInput = document.querySelector("#cantidad-modal");
    let cantidad = parseInt(cantidadInput.value);
    cantidad += incremento;
    if (cantidad >= 1) {
        cantidadInput.value = cantidad;
    }
}

function abrirLupa(imagen, titulo, precio) {
    const modal = document.getElementById('modalLupa1'); // O modalLupa2 según sea necesario
    modal.style.display = 'flex'; // Mostrar el modal
    document.getElementById('imagen-modal').src = imagen; // Cambiar la imagen en el modal
    document.getElementById('titulo').textContent = titulo; // Cambiar el título en el modal
    document.getElementById('precio-modal').textContent = precio; // Cambiar el precio en el modal
    
}

// Función para cerrar el modal de lupa
function cerrarLupa() {
    const modal = document.getElementById('modalLupa1'); // O modalLupa2 según sea necesario
    modal.style.display = 'none'; // Ocultar el modal
}

// Función para actualizar la cantidad del producto
function actualizarCantidad(accion) {
    let cantidadInput = document.getElementById('cantidad');
    let cantidad = parseInt(cantidadInput.value);
    if (accion === 'mas') {
        cantidad++;
    } else if (accion === 'menos' && cantidad > 1) {
        cantidad--;
    }
    cantidadInput.value = cantidad;
}

// Función para cambiar la imagen principal en el modal según la perspectiva seleccionada
function cambiarImagen(imagen) {
    document.getElementById('imagen-modal').src = imagen;
}

// Función genérica para abrir cualquier modal pasando su ID
function abrirModal2(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "flex"; // Muestra el modal
    }
}

// Función genérica para cerrar cualquier modal pasando su ID
function cerrarModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "none"; // Oculta el modal
    }
}


function actualizarCantidad(id, accion) {
    let input = document.getElementById(id);
    let cantidad = parseInt(input.value);

    if (accion === 'sumar') {
        cantidad++;
    } else if (accion === 'restar' && cantidad > 1) {
        cantidad--;
    }

    input.value = cantidad;
}




//FORMULARIO PAGO EN DETALLES FACTURA
function mostrarFormulario(tipoPago) {
    let formularioPago = document.getElementById("formulario-pago");

    // Si ya está visible, lo oculta
    if (formularioPago.style.display === "block") {
        formularioPago.style.display = "none";
        return; // Sale de la función para cerrar el formulario
    }

    let contenido = "";

    if (tipoPago === "pse") {
        contenido = `
            <h3>Pagar con PSE</h3>
            <label for="banco" class="form-label">Selecciona tu banco</label>
            <select class="form-select" id="banco">
                <option value="bancolombia">Bancolombia</option>
                <option value="davivienda">Davivienda</option>
                <option value="bbva">BBVA</option>
                <option value="nequi">Nequi</option>
            </select>
            <button id="btnPago" class="btn">Confirmar Pago</button>
        `;
    } else if (tipoPago === "tarjeta") {
        contenido = `
            <h3>Pagar con Tarjeta</h3>
            <label for="tarjeta" class="form-label">Número de Tarjeta</label>
            <input type="text" id="tarjeta" class="form-control" placeholder="**** **** **** ****">
            <label for="cvv" class="form-label mt-2">CVV</label>
            <input type="text" id="cvv" class="form-control" placeholder="***">
            <button id="btnPago" class="btn">Confirmar Pago</button>
        `;
    } else if (tipoPago === "transferencia") {
        contenido = `
            <h3>Transferencia Bancaria</h3>
            <p>Realiza la transferencia a la cuenta #123456789 del Banco X.</p>
            <button id="btnPago" class="btn">Confirmar Pago</button>
        `;
    }

    formularioPago.innerHTML = contenido;
    formularioPago.style.display = "block"; // Muestra el formulario cuando se selecciona una opción

    // Aplicar estilo al botón
    let boton = document.getElementById("btnPago");
    boton.style.backgroundColor = "black";  // Fondo negro
    boton.style.color = "white";            // Texto blanco
    boton.style.padding = "10px 10px";
    boton.style.borderRadius = "10px";
    boton.style.fontSize = "16px";
    boton.style.border = "none";
    boton.style.cursor = "pointer";
    boton.style.width = "100%";
    boton.style.marginTop = "15px";

    // Cambio de color en hover
    boton.addEventListener("mouseover", function () {
        boton.style.backgroundColor = "#00a2ff";  // Azul claro
    });

    boton.addEventListener("mouseout", function () {
        boton.style.backgroundColor = "black";  // Regresa a negro
    });
}
