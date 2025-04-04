function mostrarFormulario(metodo) {
    const formulario = document.getElementById('formulario-pago');
    const titulo = document.getElementById('titulo-formulario');
    const extraDato = document.getElementById('extra-dato');

    // Resetear el contenido extra
    extraDato.innerHTML = '';
    extraDato.classList.add('oculto');

    // Configurar el formulario según el método de pago
    switch (metodo) {
        case 'pse':
            titulo.textContent = 'Pago por PSE';
            extraDato.innerHTML = `
                <label for="punto-pago">Selecciona el punto de pago donde quieras pagar:</label>
                <input type="text" id="punto-pago" name="punto-pago" required>
                
                <label for="tipo-documento">Tipo de documento del titular:</label>
                <select id="tipo-documento" name="tipo-documento" required>
                    <option value="CC">CC</option>
                    <option value="CE">CE</option>
                    <option value="TI">TI</option>
                </select>
                <label for="documento">Número de documento:</label>
                
                <input type="text" id="documento" name="documento" required>

                <label for="institucion-financiera">Institución Financiera:</label>
                <select id="institucion-financiera" name="institucion-financiera" required>
                    <option value="">Seleccione una institución</option>
                    <option value="bancolombia">Bancolombia</option>
                    <option value="davivienda">Davivienda</option>
                    <option value="bbva">BBVA</option>
                    <option value="colpatria">Colpatria</option>
                    <option value="nequi">Nequi</option>
                    <option value="daviplata">Daviplata</option>
                </select>
            `;
            break;
        case 'tarjeta':
            titulo.textContent = 'Pago con Tarjeta';
            extraDato.innerHTML = `
                <label for="numero-tarjeta">Número de tarjeta:</label>
                <input type="text" id="numero-tarjeta" name="numero-tarjeta" required>
                <label for="cvv">CVV:</label>
                <input type="text" id="cvv" name="cvv" required>
            `;
            extraDato.classList.remove('oculto');
            break;
        case 'transferencia':
            titulo.textContent = 'Transferencia Bancaria';
            break;
        default:
            titulo.textContent = '';
    }

    // Mostrar el formulario
    formulario.classList.add('visible');
}

// Para ocultar el formulario al cancelar o al enviar el formulario
document.getElementById('datos-pago').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Pago procesado');
    document.getElementById('formulario-pago').classList.remove('visible');
});
