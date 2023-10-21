document.getElementById('showAlert').addEventListener('click', function() {
    var alertBox = document.getElementById('customAlert');
    var alertText = document.getElementById('alertText');
    
    alertText.innerHTML = 'Это ваш кастомный Alert!';
    
    alertBox.style.display = 'block';
    
    setTimeout(function() {
        alertBox.style.display = 'none';
    }, 5000);
});