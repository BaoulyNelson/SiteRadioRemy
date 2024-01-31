// Récupérer la date actuelle
var date = new Date();

// Tableaux des noms de jours et des noms de mois en français
var jours = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"];
var mois = ["Janv", "Févr", "Mars", "Avr", "Mai", "Juin", "Juil", "Août", "Sept", "Oct", "Nov", "Déc"];

// Formater la date
var jourSemaine = jours[date.getDay()];
var jour = date.getDate();
var moisAnnee = mois[date.getMonth()];
var annee = date.getFullYear();

// Afficher la date dans la div avec l'id "date"
document.getElementById("date").textContent = jourSemaine + ". " + jour + " " + moisAnnee + " " + annee;

//l'anne a jour du footer
try {
    // Essayer d'exécuter le script
    document.getElementById("current-year").textContent = new Date().getFullYear();
  } catch (error) {
    // En cas d'erreur, afficher l'erreur dans la console
    console.error("Erreur JavaScript :", error.message);
  }