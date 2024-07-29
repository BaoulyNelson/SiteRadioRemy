// Fonction pour ouvrir ou fermer le panneau
function togglePanel() {
    var sidePanel = document.getElementById('sidePanel');
    var toggleButton = document.getElementById('togglePanel');

    // Vérifie si le panneau est ouvert
    var isOpen = sidePanel.classList.contains('show');

    if (isOpen) {
      // Si le panneau est ouvert, le ferme
      sidePanel.classList.remove('show');
      toggleButton.innerHTML = '&#9776;'; // Change l'icône en menu
    } else {
      // Si le panneau est fermé, l'ouvre
      sidePanel.classList.add('show');
      toggleButton.innerHTML = '&times;'; // Change l'icône en croix de fermeture
    }
  }
  
// Fonction pour fermer le panneau
function closePanel() {
    var sidePanel = document.getElementById('sidePanel');
    sidePanel.classList.remove('show'); // Ferme le panneau
    document.getElementById('togglePanel').innerHTML = '&#9776;'; // Change l'icône en menu
}

// Ajoute un écouteur d'événement au clic sur le bouton de bascule
document.getElementById('togglePanel').addEventListener('click', function() {
    togglePanel(); // Appelle la fonction pour ouvrir ou fermer le panneau
});

// Ajoute un écouteur d'événement au clic sur le bouton de fermeture
document.getElementById('closeButton').addEventListener('click', function() {
    closePanel(); // Appelle la fonction pour fermer le panneau
});




