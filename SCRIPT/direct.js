
// Fonction pour démarrer la diffusion en direct
function startLiveBroadcast() {
    var request = gapi.client.youtube.liveBroadcasts.insert({
      part: "snippet,status",
      resource: {
        snippet: {
          title: "Titre de votre diffusion en direct",
          scheduledStartTime: "2024-04-23T12:00:00.000Z"
        },
        status: {
          privacyStatus: "public"
        }
      }
    });
    request.execute(function(response) {
      console.log(response);
      if (response.error) {
        alert("Erreur lors du démarrage de la diffusion en direct : " + response.error.message);
      } else {
        alert("Diffusion en direct démarrée avec succès !");
      }
    });
  }
  
  // Charger l'API YouTube
  function init() {
    gapi.client.setApiKey('VOTRE_CLE_API_YOUTUBE');
    gapi.client.load('youtube', 'v3', function() {
      // API YouTube chargée, vous pouvez maintenant utiliser les fonctions de l'API
    });
  }
  