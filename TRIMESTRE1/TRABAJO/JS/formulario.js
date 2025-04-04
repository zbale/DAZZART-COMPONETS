(() => {
    'use strict';
    document.querySelector(".needs-validation").addEventListener("submit", function (event) {
        let form = event.target;
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add("was-validated");
    }, false);
})();

