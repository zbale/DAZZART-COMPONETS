var modal = document.getElementById('login-modal');
var btnOpen = document.getElementById('login-btn');  
var btnClose = document.querySelector('.close');

btnOpen.onclick = function() {
    modal.style.display = "flex";
    document.body.classList.add('modal-open');
}

btnClose.onclick = function() {
    modal.style.display = "none";
    document.body.classList.remove('modal-open');
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        document.body.classList.remove('modal-open');
    }
}