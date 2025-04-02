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
