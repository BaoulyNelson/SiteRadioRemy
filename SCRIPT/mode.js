// Fonction pour basculer entre le mode nuit et le mode jour
function toggleNightMode() {
  var body = document.body;
  body.classList.toggle('night-mode');
}

// Ajoute un écouteur d'événement au clic sur l'interrupteur
document.getElementById('customSwitch').addEventListener('click', function() {
  toggleNightMode(); // Appelle la fonction pour basculer entre les modes
});
