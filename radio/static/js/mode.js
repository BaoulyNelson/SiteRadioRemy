function toggleTheme() {
  const body = document.body;
  const themeIcon = document.getElementById("theme-icon");
  const themeText = document.getElementById("theme-text");

  body.classList.toggle("dark-mode");

  if (body.classList.contains("dark-mode")) {
      themeIcon.textContent = "☀️";  // Icône de soleil pour le mode jour
      themeText.textContent = "Mode Jour";
      localStorage.setItem("theme", "dark");
  } else {
      themeIcon.textContent = "🌙";  // Icône de lune pour le mode nuit
      themeText.textContent = "Mode Nuit";
      localStorage.setItem("theme", "light");
  }
}

// Applique le thème enregistré et met à jour le texte lors du chargement de la page
window.onload = function() {
  const savedTheme = localStorage.getItem("theme");
  const themeIcon = document.getElementById("theme-icon");
  const themeText = document.getElementById("theme-text");

  if (savedTheme && savedTheme === "dark") {
      document.body.classList.add("dark-mode");
      themeIcon.textContent = "☀️";  // Icône de soleil pour le mode jour
      themeText.textContent = "Mode Jour";
  } else {
      themeIcon.textContent = "🌙";  // Icône de lune pour le mode nuit
      themeText.textContent = "Mode Nuit";
  }
}
