function handleNavLinkClick(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        var target = link.getAttribute('data-target');
        var section = document.getElementById(target);

        // Masquer tous les contenus
        var sections = document.querySelectorAll('section');
        sections.forEach(function(section) {
            section.style.display = 'none';
        });

        // Afficher le contenu spécifique au lien sélectionné
        section.style.display = 'block';

        // Fermer le panneau latéral (à adapter selon votre structure HTML)
        document.getElementById('side-panel').style.width = '0';
        document.body.classList.remove('no-scroll');
    });
}

function initNavigation() {
    var sidePanelLinks = document.querySelectorAll('#side-panel a'); // Sélectionner les liens du panneau latéral uniquement
    sidePanelLinks.forEach(function(link) {
        handleNavLinkClick(link);
    });

    var navLinks = document.querySelectorAll('nav a'); // Sélectionner les liens de navigation principale
    navLinks.forEach(function(link) {
        handleNavLinkClick(link);
    });
}

document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('side-panel').style.width = '0';
    document.body.classList.remove('no-scroll');
});

// Appeler la fonction initNavigation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
});
