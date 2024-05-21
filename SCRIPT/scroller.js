// Afficher ou masquer la flèche pour remonter
window.onscroll = function() { 
    scrollFunction(); 
    checkScrollDirection(); 
};


// Fonction pour remonter en haut de la page
function scrollToTop() {
    document.documentElement.scrollTo({
        top: 0,
        behavior: 'smooth' // Pour un défilement fluide
    });
}

function scrollFunction() {
    const arrowTop = document.getElementById("arrowTop");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        arrowTop.style.display = "block";
    } else {
        arrowTop.style.display = "none";
    }
}

// Vérifier la direction du scroll pour afficher ou masquer le footer
var lastScrollTop = 0;
function checkScrollDirection() {
    var footer = document.querySelector('footer');
    var currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        // Scroll vers le bas
        footer.classList.add('hidden-footer');
    } else {
        // Scroll vers le haut
        footer.classList.remove('hidden-footer');
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Pour Mobile ou scroll négatif
}
