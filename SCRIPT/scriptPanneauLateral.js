document.getElementById('menu-icon').addEventListener('click', function() {
    document.getElementById('side-panel').style.width = '250px';
    document.body.classList.add('no-scroll'); // Ajoutez la classe au corps
});

document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('side-panel').style.width = '0';
    document.body.classList.remove('no-scroll'); // Retirez la classe au corps
});
