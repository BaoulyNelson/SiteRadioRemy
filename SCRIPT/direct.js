// Contenu du fichier externe (par exemple, twitch_embed.js)

// Assurez-vous que Twitch est chargé avant d'exécuter ce code
if (typeof Twitch !== 'undefined') {
  new Twitch.Embed("twitch-embed", {
      channel: "BaoulyNelson",
      layout: "video",
      height: 360, // Hauteur minimale recommandée pour une vidéo en 16:9
      width: 640   // Largeur minimale recommandée
  });
} else {
  console.error("Twitch n'est pas chargé correctement.");
}
