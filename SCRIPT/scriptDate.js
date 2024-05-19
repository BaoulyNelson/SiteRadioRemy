
function updateTime() {
    const currentTimeElement = document.getElementById("current-time");
    const now = new Date();

    // Jours de la semaine et mois
    const daysOfWeek = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
    const months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];

    const dayOfWeek = daysOfWeek[now.getDay()];
    const dayOfMonth = now.getDate().toString().padStart(2, '0');
    const month = months[now.getMonth()];
    const year = now.getFullYear();


    const currentTimeString = `${dayOfWeek} ${dayOfMonth} ${month} ${year}`;
    currentTimeElement.textContent = currentTimeString;
}

// Mettez à jour l'heure chaque seconde
setInterval(updateTime, 1000);

// Appelez updateTime une fois pour afficher l'heure initiale
updateTime();
