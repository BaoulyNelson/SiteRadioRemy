var lastScrollTop = 0;
window.addEventListener('scroll', function() {
  var footer = document.querySelector('footer');
  var currentScroll = window.pageYOffset || document.documentElement.scrollTop;

  if (currentScroll > lastScrollTop) {
    // Scroll vers le bas
    footer.classList.add('hidden-footer');
  } else {
    // Scroll vers le haut
    footer.classList.remove('hidden-footer');
  }

  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Pour Mobile ou scroll négatif
}, false);