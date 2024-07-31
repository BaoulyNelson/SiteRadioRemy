  // Fonction pour basculer entre le mode nuit et le mode jour
  function toggleNightMode() {
    var body = document.body;
    body.classList.toggle('night-mode');

    // Changer l'icône du mode et le texte
    var modeIcon = document.getElementById('modeIcon');
    var modeText = document.getElementById('modeText');
    if (body.classList.contains('night-mode')) {
      modeIcon.innerHTML = '<i class="fas fa-moon"></i>';
      modeText.innerText = 'Mode jour';
    } else {
      modeIcon.innerHTML = '<i class="fas fa-sun"></i>';
      modeText.innerText = 'Mode nuit';
    }
  }

  // Ajoute un écouteur d'événement au clic sur l'interrupteur
  document.getElementById('customSwitch').addEventListener('click', function() {
    toggleNightMode(); // Appelle la fonction pour basculer entre les modes
  });
