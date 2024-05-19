function showSection(sectionId) {
    // Masquer toutes les sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.style.display = 'none';
    });

    // Afficher la section sélectionnée
    const selectedSection = document.getElementById(sectionId);
    selectedSection.style.display = 'block';
}

const audioPlayer = document.getElementById('audio-player');
const playButton = document.getElementById('play');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const trackTitle = document.getElementById('track-title');

let isPlaying = false;

function playTrack(trackIndex) {
    // Pour cette simulation, une seule piste est utilisée.
    audioPlayer.src = "path/to/your/music/file.mp3";
    audioPlayer.play();
    isPlaying = true;
    playButton.innerHTML = '&#10074;&#10074;';
    trackTitle.textContent = "Geva Alon - In The Morning Light";  // Mettez à jour avec le titre de la piste
}

playButton.addEventListener('click', () => {
    if (isPlaying) {
        audioPlayer.pause();
        playButton.innerHTML = '&#9654;';
    } else {
        audioPlayer.play();
        playButton.innerHTML = '&#10074;&#10074;';
    }
    isPlaying = !isPlaying;
});

prevButton.addEventListener('click', () => {
    // Ajouter la logique pour passer à la piste précédente
});

nextButton.addEventListener('click', () => {
    // Ajouter la logique pour passer à la piste suivante
});

// Ajouter plus de pistes si nécessaire
