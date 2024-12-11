<script>
    function showSection(sectionId) {
        
        document.getElementById('description').style.display = 'none';
        document.getElementById('additional-info').style.display = 'none';
        document.getElementById('reviews').style.display = 'none';

        var buttons = document.querySelectorAll('.product-buttons button');
        buttons.forEach(function(button) {
            button.classList.remove('active')
        });

        document.getElementById(sectionId).style.display = 'block';

        var activeButton = document.querySelector('.product-buttons button[onclick="showSection(\'' + sectionId + '\')"]');
        activeButton.classList.add('active');
    }
</script>