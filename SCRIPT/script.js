document.getElementById('togglePanel').addEventListener('click', function() {
    var sidePanel = document.getElementById('sidePanel');
    if (sidePanel.style.left === '0px') {
      sidePanel.style.left = '-250px';
      document.getElementById('togglePanel').innerHTML = '&#9776;';
    } else {
      sidePanel.style.left = '0';
      document.getElementById('togglePanel').innerHTML = '&times;';
    }
  });
  
  document.getElementById('closeButton').addEventListener('click', function() {
    var sidePanel = document.getElementById('sidePanel');
    sidePanel.style.left = '-250px';
    document.getElementById('togglePanel').innerHTML = '&#9776;';
  });
  
  $('#customSwitch').change(function() {
    if ($(this).is(':checked')) {
      $('body').addClass('dark-mode');
    } else {
      $('body').removeClass('dark-mode');
    }
  });
  

  // Ajoutez ce code à votre fichier JavaScript ou dans une balise <script> dans votre HTML
document.addEventListener("DOMContentLoaded", function () {
  var button = document.getElementById('backToTopBtn');

  // Affiche ou masque la flèche en fonction du défilement
  window.onscroll = function () {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
          button.style.display = 'block';
      } else {
          button.style.display = 'none';
      }
  };

  // Fait défiler la page vers le haut lorsque la flèche est cliquée
  button.addEventListener('click', function () {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
  });
});


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

function toggleContent(contentId) {
  // Masquer toutes les sections de contenu
  var sections = document.getElementsByClassName("content-section");
  for (var i = 0; i < sections.length; i++) {
      sections[i].classList.add("hidden");
  }
  
  // Afficher la section de contenu spécifique
  var content = document.getElementById(contentId + "Content");
  content.classList.remove("hidden");
}
