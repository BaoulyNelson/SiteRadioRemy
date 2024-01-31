// Contenu du fichier script.js
// Vérifie s'il y a du contenu dans au moins l'une des sections avec la classe 'content-section'
var contentSections = document.querySelectorAll('.content-section');
var footerDiv = document.getElementById('footer');
var contentFound = false;

for (var i = 0; i < contentSections.length; i++) {
    if (contentSections[i].innerHTML.trim() !== '') {
        // Si du contenu est présent dans au moins l'une des sections, affiche le footer et arrête la boucle
        contentFound = true;
        break;
    }
}

if (contentFound) {
    footerDiv.style.display = 'block';
}
