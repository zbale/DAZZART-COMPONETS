document.getElementById('facturacion-form').addEventListener("submit", function(event) {
    event.preventDefault(); 

    const producto = "Torre Wevo Ranchero × 1";
    const subtotal = "6.799.990";
    const total = "6.799.990";
    const detallesPedido = `
        <tr>
            <td>${producto}</td>
            <td>$ ${subtotal}</td>
        </tr>
    `;
 
    document.getElementById('detalle-producto').innerHTML = detallesPedido;
    document.getElementById('subtotal').textContent = `$ ${subtotal}`;
    document.getElementById('total').textContent = `$ ${total}`;

    // Mostrar el resumen de la factura
    document.getElementById('resumen-pedido').style.display = "block";
});
