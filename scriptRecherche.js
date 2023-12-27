document.getElementById("search").addEventListener("input", function () {
    var clearSearchIcon = document.getElementById("clear-search");
    var searchInput = document.getElementById("search");

    if (searchInput.value.length > 0) {
        clearSearchIcon.style.display = "inline"; // Affiche l'icône de croix lorsque du texte est présent
    } else {
        clearSearchIcon.style.display = "none"; // Masque l'icône de croix lorsque la barre de recherche est vide
    }
});

function clearSearch() {
    document.getElementById("search").value = ""; // Efface le contenu de la barre de recherche
    document.getElementById("clear-search").style.display = "none"; // Masque l'icône de croix
  // Masque ou supprime le contenu associé à l'ancre d'un lien
  hideOrRemoveContent(); // Appel de votre fonction pour masquer ou supprimer le contenu

}
// Fonction pour masquer le contenu associé à l'ancre d'un lien
function hideOrRemoveContent() {
    // Sélectionnez tous les éléments de contenu (assurez-vous qu'ils ont une classe ou un attribut permettant de les identifier)
    var contentSections = document.querySelectorAll('.content-section');

    // Masquez ou supprimez chaque élément de contenu
    contentSections.forEach(function(contentSection) {
        contentSection.style.display = "none"; // Modifiez cela selon vos besoins, vous pouvez également utiliser remove() pour le supprimer du DOM
    });
}

