document.getElementById("config-btn").addEventListener("click", function (e) {
    e.preventDefault();
    const configMenu = document.querySelector(".config-menu");
    configMenu.style.display = configMenu.style.display === "block" ? "none" : "block";
});


document.addEventListener('DOMContentLoaded', () => {
 
    const deleteButtons = document.querySelectorAll('.delete-btn');
  
    deleteButtons.forEach(button => {
      button.addEventListener('click', () => {
        Swal.fire({
          title: '¿Desea eliminar?',
          text: 'Esta acción no se puede deshacer.',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#d33',
          cancelButtonColor: '#3085d6',
          confirmButtonText: 'Sí, eliminar',
          cancelButtonText: 'No, cancelar'
        }).then((result) => {
          if (result.isConfirmed) {
          
            window.location.href = 'archivos html/confirmarEliminacion.html';
          } else if (result.dismiss === Swal.DismissReason.cancel) {
            window.location.href = 'archivos html/cancelarEliminacion.html';
          }
        });
      });
    });
  });