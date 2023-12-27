// Ajoutez une fonction pour faire défiler la page vers la section cible
function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: "smooth" });
    }
}

function toggleMenu() {
    var menuList = document.getElementById("menu-list");
    if (menuList.style.display === "none" || menuList.style.display === "") {
        menuList.style.display = "block";
    } else {
        menuList.style.display = "none";
    }
}

// Ajoutez des gestionnaires d'événements pour chaque lien du menu
var menuLinks = document.querySelectorAll("#menu-list li a");
menuLinks.forEach(function (link) {
    link.addEventListener("click", function (event) {
        event.preventDefault();
        var targetSectionId = link.getAttribute("href").substring(1);
        showContent(targetSectionId);
    });
});

var currentSectionIndex = 0;
var sections = document.querySelectorAll('.content-section');

function showPreviousContent() {
    if (currentSectionIndex > 0) {
        sections[currentSectionIndex].style.display = 'none';
        currentSectionIndex--;
        sections[currentSectionIndex].style.display = 'block';
    }
}

function showNextContent() {
    if (currentSectionIndex < sections.length - 1) {
        sections[currentSectionIndex].style.display = 'none';
        currentSectionIndex++;
        sections[currentSectionIndex].style.display = 'block';
    }
}

// Fonction pour compter les occurrences du mot dans le champ de recherche
function countOccurrences() {
    var searchTerm = document.getElementById("search").value.toLowerCase();

    // Vérifier si l'utilisateur a tapé quelque chose
    if (searchTerm.trim() === "") {
        // Si le champ est vide, ne rien afficher
        clearOccurrencesDisplay();
        return;
    }

    var content = document.body.textContent.toLowerCase();
    var occurrences = content.split(searchTerm).length - 1;

    // Afficher le nombre d'occurrences
    var occurrencesDisplay = document.getElementById("occurrences-display");
    occurrencesDisplay.textContent = occurrences + " Mots trouvés  ";

    // Vérifier si le terme de recherche correspond à l'ancre d'un lien
    var linkAnchors = document.querySelectorAll('#menu-list li a');
    linkAnchors.forEach(function (linkAnchor) {
        var linkText = linkAnchor.textContent.toLowerCase();
        if (linkText.includes(searchTerm)) {
            // Si le terme de recherche fait partie d'un lien, afficher le contenu associé
            var sectionId = linkAnchor.getAttribute("href").substring(1);
            showContent(sectionId);
        }
    });
}

// Fonction pour effacer l'affichage des occurrences
function clearOccurrencesDisplay() {
    var occurrencesDisplay = document.getElementById("occurrences-display");
    occurrencesDisplay.textContent = "";
}

// Fonction pour afficher le contenu de la section spécifiée
function showContent(sectionId) {
    // Masquer tous les contenus au début
    hideAllContents();

    var targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.style.display = 'block'; // Afficher le contenu associé

        // Si la section cible a la classe .containt, l'afficher également
        if (targetSection.classList.contains('containt')) {
            var containtContent = document.querySelector('.containt');
            if (containtContent) {
                containtContent.style.display = 'block';
            }
        }

        scrollToSection(sectionId);
    }
}

// Fonction pour masquer tous les contenus
function hideAllContents() {
    var allContents = document.querySelectorAll('.content-section');
    allContents.forEach(function (content) {
        content.style.display = 'none';
    });

    // Masquer le contenu dans la classe .containt
    var containtContent = document.querySelector('.containt');
    if (containtContent) {
        containtContent.style.display = 'none';
    }
}

// Ajoutez le script JavaScript pour faire défiler la page vers le haut
document.querySelector('.enhaut').addEventListener('click', function (e) {
    e.preventDefault();
    document.body.scrollTop = 0; // Pour les navigateurs plus anciens
    document.documentElement.scrollTop = 0; // Pour les navigateurs modernes
});
