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
