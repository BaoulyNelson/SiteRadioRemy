  // Fonction pour obtenir la date en format français
  function getDateFrancais() {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const date = new Date();
    return date.toLocaleDateString('fr-FR', options);
}

// Fonction pour mettre à jour la date en temps réel
function updateDate() {
    const dateElement = document.getElementById('date-actuelle');
    if (dateElement) {
        dateElement.textContent = getDateFrancais();
    }
}

// Mettre à jour la date au chargement de la page
window.onload = function () {
    updateDate();
    // Mettre à jour la date toutes les secondes
    setInterval(updateDate, 1000);
};