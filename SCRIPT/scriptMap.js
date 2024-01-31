 // Code JavaScript pour initialiser la carte
 var map = L.map('map').setView([18.9712, -72.2852], 8); // Coordonnées centrées sur Haïti et zoom initial

 L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
   attribution: '© OpenStreetMap contributors'
 }).addTo(map);

 function toggleMenu() {
  var nav = document.querySelector('nav');
  nav.classList.toggle('show'); // Ajoute ou supprime la classe 'show'
  nav.classList.toggle('vertical'); // Ajoute ou supprime la classe 'vertical'

  // Ajouter ou supprimer la classe 'open' pour changer l'icône du menu
  var menuIcon = document.getElementById('menu-icon');
  menuIcon.classList.toggle('open');

  // Afficher ou masquer l'icône de croix
  var closeIcon = document.getElementById('close-icon');
  closeIcon.style.display = (closeIcon.style.display === 'flex') ? 'none' : 'flex';
}
