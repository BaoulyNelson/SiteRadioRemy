// Fonction pour calculer la hauteur du footer
function getFooterHeight() {
    const footer = document.querySelector('footer');
    return footer ? footer.offsetHeight : 0;
}

function loadMoreContent() {
    // Simule le chargement de contenu supplémentaire
    const newContent = document.createElement('div');
    newContent.className = 'post';
    newContent.innerHTML = '<h2>Autre Contenu</h2><p>Contenu en cours de chargement...</p>';
    document.querySelector('main').appendChild(newContent);
}


// Ajout d'un événement de défilement de la fenêtre
window.addEventListener('scroll', () => {
    // Vérifie si l'utilisateur a fait défiler jusqu'au bas de la page
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        // Chargez plus de contenu
        loadMoreContent();
    }
});


document.addEventListener("DOMContentLoaded", function() {
    var footer = document.querySelector(".footer");
    var lastScrollTop = 0;

    window.addEventListener("scroll", function() {
        var currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop) {
            // Scrolling down
            footer.classList.add("footer-hidden");
            footer.classList.remove("footer-visible");
        } else {
            // Scrolling up
            footer.classList.remove("footer-hidden");
            footer.classList.add("footer-visible");
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
    }, false);
});
