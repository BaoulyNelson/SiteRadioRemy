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