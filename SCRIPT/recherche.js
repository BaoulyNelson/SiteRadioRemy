document.addEventListener('DOMContentLoaded', function () {
    var searchButton = document.getElementById('searchButton');
    var recherche = document.getElementById('recherche');
    var apercuRecherche = document.getElementById('apercu-recherche');
    var inputRecherche = recherche.querySelector('input');
    var resultMessage = document.getElementById('result-message');

    // Placer le focus dans la barre de recherche lors du clic sur l'icône de recherche
    searchButton.addEventListener('click', function () {
        recherche.style.display = (recherche.style.display === 'none' || recherche.style.display === '') ? 'block' : 'none';
        inputRecherche.focus(); // Mettre le focus dans la barre de recherche
    });

    // Gérer les changements dans la barre de recherche
    inputRecherche.addEventListener('input', function () {
        var searchTerm = inputRecherche.value.toLowerCase();
        var hasResults = false; // Variable pour vérifier si la recherche a des résultats

        // Mettre à jour l'aperçu si le terme de recherche n'est pas vide
        if (searchTerm.trim() !== '') {
            apercuRecherche.innerHTML = "";

            // Parcourir les liens pour filtrer en fonction du terme de recherche
            var links = document.querySelectorAll('ul li a');
            links.forEach(function (link) {
                var linkTitle = link.title.toLowerCase();
                if (linkTitle.includes(searchTerm)) {
                    var dataTarget = link.getAttribute('data-target');
                    var correspondingSection = document.getElementById(dataTarget);

                    if (correspondingSection) {
                        correspondingSection.classList.remove('hidden');
                        hasResults = true;

                        // Transformer l'aperçu en un lien cliquable
                        var sectionTitle = correspondingSection.querySelector('h2').textContent;
                        var previewLink = document.createElement('a');
                        previewLink.href = '#' + dataTarget;
                        previewLink.textContent = sectionTitle;

                        // Ajouter un gestionnaire d'événements pour le lien généré
                        previewLink.addEventListener('click', function (event) {
                            event.preventDefault(); // Empêcher le comportement par défaut du lien
                            // Ajouter ici tout code supplémentaire que vous souhaitez exécuter avant de rediriger
                            window.location.href = previewLink.href; // Rediriger vers le contenu correspondant
                        });

                        apercuRecherche.appendChild(previewLink);
                    }
                } else {
                    var dataTarget = link.getAttribute('data-target');
                    var correspondingSection = document.getElementById(dataTarget);

                    if (correspondingSection) {
                        correspondingSection.classList.add('hidden');
                    }
                }
            });
        } else {
            apercuRecherche.innerHTML = ""; // Réinitialiser l'aperçu si le terme de recherche est vide
        }

        // Afficher le message de résultat en fonction de la recherche
        resultMessage.textContent = hasResults ? '' : 'Aucun résultat trouvé';
    });
});

function fermerRecherche() {
    var recherche = document.getElementById('recherche');
    recherche.style.display = 'none';
}
