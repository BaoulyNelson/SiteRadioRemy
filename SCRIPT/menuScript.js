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
    });
}

function initNavigation() {
    var links = document.querySelectorAll('nav a');
    links.forEach(function(link) {
        handleNavLinkClick(link);
    });
}

// Appeler la fonction initNavigation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
});
