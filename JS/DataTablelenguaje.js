$(document).ready(function() {
  $('#example').DataTable({
      "language": {
          "sSearch": "Buscar:",
          "sLengthMenu": "Mostrar _MENU_ entradas",
          "sInfo": "Mostrando _START_ a _END_ de _TOTAL_ entradas",
          "sInfoEmpty": "Mostrando 0 a 0 de 0 entradas",
          "sInfoFiltered": "(filtrado de _MAX_ entradas en total)",
          "sInfoPostFix": "",
          "sSearchPlaceholder": "Buscar...",
          "oPaginate": {
              "sFirst": "Primero",
              "sPrevious": "Anterior",
              "sNext": "Siguiente",
              "sLast": "Último"
          }
      }
  });
});
