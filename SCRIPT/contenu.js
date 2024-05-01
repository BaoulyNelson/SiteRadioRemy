// Fonction pour masquer et afficher les contenus
function toggleContent(contentId) {
    var content = document.getElementById(contentId);
    // Masquer tous les contenus à l'intérieur de la balise <main> et de la classe .contenu
    var allContents = document.querySelectorAll('main .contenu');
    for (var i = 0; i < allContents.length; i++) {
        allContents[i].style.display = 'none';
    }
    // Masquer le jumbotron
    var jumbotron = document.querySelector('.jumbotron');
    jumbotron.style.display = 'none';
    // Afficher le contenu associé au lien cliqué
    content.style.display = 'block';
}
