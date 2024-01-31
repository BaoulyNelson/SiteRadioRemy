function displayFileName(input) {
    const customLabel = document.getElementById('customLabel');
    if (input.files.length > 0) {
      customLabel.textContent = input.files[0].name;
    } else {
      customLabel.textContent = 'Choisir un fichier';
    }
  }

    // Afficher le modal d'inscription lorsque l'utilisateur clique sur "Inscrivez-vous"
    document.getElementById('showRegister').addEventListener('click', function () {
        $('#loginModal').modal('hide');
        $('#registerModal').modal('show');
      });