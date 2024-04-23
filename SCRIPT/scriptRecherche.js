document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("mySearch");
  const menuItems = document.querySelectorAll(".menu li");
  const categoryItems = document.querySelectorAll(".categories li");
  const searchIcon = document.getElementById("searchIcon");
  const searchForm = document.getElementById("searchForm");

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
// Fonction pour afficher le message avec le résultat
function showResultMessage(found) {
  const resultMessage = document.getElementById("resultMessage");
  resultMessage.textContent = found ? "Un lien a été trouvé." : "Aucun lien trouvé.";
  resultMessage.style.display = "block"; // Afficher le message
}

  // Ajouter un événement de saisie pour détecter les changements dans le champ de recherche
  searchInput.addEventListener("input", function(event) {
      const searchText = event.target.value.toLowerCase();
      filterItems(searchText);
  });
});

