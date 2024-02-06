const searchIcon = document.getElementById('searchIcon');
const searchPreview = document.getElementById('searchPreview');
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');
const noResultsMessage = document.getElementById('noResultsMessage');

searchIcon.addEventListener('click', function() {
    // Afficher le formulaire de recherche et le panneau latéral
    searchPreview.style.display = 'block';
    document.getElementById('side-panel').style.display = 'block';

    // Effacer les résultats précédents
    searchResults.innerHTML = '';

    // Ajouter un écouteur d'événements pour le champ de recherche
    searchInput.addEventListener('input', searchLinks);
});

function searchLinks() {
    const searchTerm = searchInput.value.trim().toLowerCase();

    // Effacer les résultats précédents
    searchResults.innerHTML = '';

    if (searchTerm === '') {
        return;
    }

    const links = document.querySelectorAll('#side-panel a');

    let resultsFound = false;

    links.forEach(link => {
        const linkText = link.textContent.trim().toLowerCase();

        if (linkText.includes(searchTerm)) {
            resultsFound = true;
            const li = document.createElement('li');
            li.innerHTML = link.outerHTML;
            searchResults.appendChild(li);
        }
    });

    if (resultsFound) {
        noResultsMessage.style.display = 'none';
    } else {
        noResultsMessage.style.display = 'block';
    }
}

searchInput.addEventListener('keyup', function(event) {
    if (event.keyCode === 8 && searchInput.value === '') { // Vérifie si la touche pressée est la touche de suppression (Backspace) et que la zone de recherche est vide
        // Cacher le formulaire de recherche
        searchPreview.style.display = 'none';

        // Réinitialiser les résultats de la recherche et le message d'aucun résultat
        searchResults.innerHTML = '';
        noResultsMessage.style.display = 'none';
    }
});
