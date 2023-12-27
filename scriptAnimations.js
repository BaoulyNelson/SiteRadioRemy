// JavaScript pour l'animation d'apparition des lettres avec couleurs et fond
document.addEventListener('DOMContentLoaded', function () {
    var elements = document.querySelectorAll('.content-section h4');

    elements.forEach(function (element, index) {
        var words = element.textContent.trim().split(' ');

        var spanWords = words.map(function (word, wordIndex) {
            var span = document.createElement('span');
            var letters = word.split('');

            var spanLetters = letters.map(function (letter, letterIndex) {
                var subSpan = document.createElement('span');
                subSpan.textContent = letter;
                subSpan.style.animationDelay = (letterIndex * 0.1) + 's';
                return subSpan;
            });

            spanLetters.forEach(function (subSpan) {
                span.appendChild(subSpan);
            });

            if (wordIndex < words.length - 1) {
                span.innerHTML += '&nbsp;'; // Ajoute un espace entre les mots
            }

            return span;
        });

        element.innerHTML = '';
        spanWords.forEach(function (span) {
            element.appendChild(span);
        });

        element.classList.add('wordFadeIn');
    });
});
