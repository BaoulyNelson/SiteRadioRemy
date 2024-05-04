const text = "RADIO MARBIAL FM 99.5";

setInterval(function() {
  const animatedText = document.getElementById("animatedText");
  animatedText.innerHTML = ""; // Effacer le contenu du texte
  
  let i = 0;
  const intervalId = setInterval(function() {
    if (i >= text.length) {
      clearInterval(intervalId); // Arrêter l'animation une fois que toutes les lettres sont affichées
    } else {
      const randomColor = getRandomColor(); // Générer une couleur aléatoire
      animatedText.innerHTML += `<span style="color: ${randomColor};">${text[i]}</span>`;
      i++;
    }
  }, 100); // Intervalle de temps entre chaque affichage de lettre (en millisecondes)
}, 3000); // Intervalle de temps entre chaque changement de couleur (en millisecondes)

function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}