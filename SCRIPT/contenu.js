// Fonction pour afficher la section sélectionnée
function showSection(sectionId) {
    // Cacher toutes les sections
    const sections = document.querySelectorAll('.container');
    sections.forEach(section => section.classList.remove('active'));

    // Afficher la section sélectionnée
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.classList.add('active');
    }

    // Masquer le footer lorsque une section est affichée
    var footer = document.querySelector('footer');
    footer.classList.add('hidden-footer');
}

// Appeler showSection() une fois que le document est chargé
document.addEventListener("DOMContentLoaded", function() {
    // Afficher "accueil" par défaut
    showSection('accueil');

    // Afficher le footer par défaut
    var footer = document.querySelector('footer');
    footer.classList.remove('hidden-footer');
});
