function showSection(sectionId) {
    // Hide all sections
    var sections = document.getElementsByClassName('section-content');
    for (var i = 0; i < sections.length; i++) {
        sections[i].classList.remove('active');
    }

    // Show the clicked section
    document.getElementById(sectionId).classList.add('active');
}


