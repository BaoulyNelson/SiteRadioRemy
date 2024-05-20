function showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('.container');
    sections.forEach(section => section.classList.remove('active'));

    // Show the selected section
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.classList.add('active');
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Show "accueil" by default
    showSection('accueil');
});