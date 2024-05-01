document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("mySearch");
    const menuItems = document.querySelectorAll(".menu li");
    const categoryItems = document.querySelectorAll(".categories li");
    const searchIcon = document.getElementById("searchIcon");
    const searchForm = document.getElementById("searchForm");
    const contentDisplay = document.getElementById("contentDisplay"); // Ajout
  
    // Afficher/masquer le formulaire de recherche lorsque l'icône est cliquée
    searchIcon.addEventListener("click", function() {
        if (searchForm.style.display === "none" || searchForm.style.display === "") {
            searchForm.style.display = "block";
            searchInput.focus(); // Définir le focus sur le champ de recherche
        } else {
            searchForm.style.display = "none";
        }
    });
  
    // Fonction pour filtrer les éléments en fonction de la saisie de l'utilisateur
    function filterItems(searchText) {
        // Filtrer les éléments du menu
        menuItems.forEach(function(item) {
            const menuItemText = item.textContent.toLowerCase();
            if (menuItemText.includes(searchText)) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
  
        // Filtrer les éléments des catégories
        categoryItems.forEach(function(item) {
            const categoryItemText = item.textContent.toLowerCase();
            if (categoryItemText.includes(searchText)) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    }
  
    function showContent(link) {
        // Création d'une instance de l'objet XMLHttpRequest
        var xhr = new XMLHttpRequest();
    
        // Définition de la fonction de rappel pour gérer la réponse de la requête
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Si la requête est réussie (statut 200), affiche le contenu de la réponse
                    contentDisplay.innerHTML = xhr.responseText;
                } else {
                    // En cas d'erreur, affiche un message d'erreur
                    contentDisplay.textContent = "Erreur : Impossible de charger le contenu associé au lien.";
                }
            }
        };
    
        // Ouverture de la requête AJAX avec la méthode GET et le lien spécifié
        xhr.open("GET", link, true);
    
        // Envoi de la requête
        xhr.send();
    }
    
  
    // Ajouter un événement de soumission pour le formulaire de recherche
    searchForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Empêcher le formulaire de se soumettre normalement
  
        const searchText = searchInput.value.trim(); // Obtenir la valeur de recherche
        // Vérifier si la valeur est un lien valide
        if (searchText.startsWith("http://") || searchText.startsWith("https://")) {
            showContent(searchText); // Afficher le contenu associé au lien
        } else {
            // Afficher un message d'erreur si ce n'est pas un lien valide
            contentDisplay.textContent = "Erreur : Veuillez entrer un lien valide.";
        }
    });
  
    // Ajouter un événement de saisie pour détecter les changements dans le champ de recherche
    searchInput.addEventListener("input", function(event) {
        const searchText = event.target.value.toLowerCase();
        filterItems(searchText);
    });
  });
  