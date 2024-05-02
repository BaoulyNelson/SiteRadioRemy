document.addEventListener("DOMContentLoaded", function() {
    var cookieNotification = document.getElementById('cookie-notification');
    var acceptCookiesBtn = document.getElementById('accept-cookies-btn');
    
    acceptCookiesBtn.addEventListener('click', function() {
        cookieNotification.style.display = 'none';
        // Ajoutez ici le code pour enregistrer la préférence de l'utilisateur concernant les cookies, par exemple en utilisant localStorage ou en créant un cookie.
    });
});
