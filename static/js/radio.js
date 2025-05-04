document.getElementById("year").textContent = new Date().getFullYear();

// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById("mobile-menu-btn");
const closeMenuBtn = document.getElementById("close-menu");
const mobileMenu = document.getElementById("mobile-menu");

mobileMenuBtn.addEventListener("click", () => {
  mobileMenu.classList.add("active");
});

closeMenuBtn.addEventListener("click", () => {
  mobileMenu.classList.remove("active");
});

// Schedule Tabs
const scheduleTabs = document.querySelectorAll(".schedule-tab");
const scheduleDays = document.querySelectorAll(".schedule-day");

scheduleTabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    // Remove active class from all tabs
    scheduleTabs.forEach((t) => t.classList.remove("active"));
    // Add active class to clicked tab
    tab.classList.add("active");

    // Hide all schedule days
    scheduleDays.forEach((day) => day.classList.remove("active"));
    // Show the selected day
    const dayId = tab.getAttribute("data-day");
    document.getElementById(dayId).classList.add("active");
  });
});

// Audio Player
const playBtn = document.getElementById("play-btn");
const playIcon = document.getElementById("play-icon");
let isPlaying = false;

playBtn.addEventListener("click", togglePlay);

function togglePlay() {
  isPlaying = !isPlaying;
  if (isPlaying) {
    playIcon.classList.remove("fa-play");
    playIcon.classList.add("fa-pause");
    // Start audio visualizer animation
    startVisualizer();
  } else {
    playIcon.classList.remove("fa-pause");
    playIcon.classList.add("fa-play");
    // Stop audio visualizer animation
    stopVisualizer();
  }
}

// Listen Live Button
const listenLiveBtn = document.getElementById("listen-live");
listenLiveBtn.addEventListener("click", (e) => {
  e.preventDefault();
  if (!isPlaying) {
    togglePlay();
  }
  // Scroll to player section
  const playerSection = document.querySelector(".player-section");
  playerSection.scrollIntoView({ behavior: "smooth" });
});

// Audio Visualizer
const visualizer = document.getElementById("visualizer");
let visualizerBars = [];
let animationFrame;

// Create visualizer bars
function createVisualizer() {
  // Clear existing bars
  visualizer.innerHTML = "";
  visualizerBars = [];

  // Create new bars
  const barCount = 50;
  for (let i = 0; i < barCount; i++) {
    const bar = document.createElement("div");
    bar.className = "visualizer-bar";
    visualizer.appendChild(bar);
    visualizerBars.push(bar);
  }
}

// Animate visualizer
function animateVisualizer() {
  for (let i = 0; i < visualizerBars.length; i++) {
    const height = Math.floor(Math.random() * 45) + 5;
    visualizerBars[i].style.height = `${height}px`;
  }
  animationFrame = requestAnimationFrame(animateVisualizer);
}

// Start visualizer
function startVisualizer() {
  if (visualizerBars.length === 0) {
    createVisualizer();
  }
  animateVisualizer();
}

// Stop visualizer
function stopVisualizer() {
  cancelAnimationFrame(animationFrame);
  visualizerBars.forEach((bar) => {
    bar.style.height = "5px";
  });
}

// Initialize visualizer
createVisualizer();

// Contact Form Submission
const contactForm = document.getElementById("contactForm");
contactForm.addEventListener("submit", (e) => {
  e.preventDefault();
  // Here you would normally send the form data to your server
  alert(
    "Merci pour votre message ! Nous vous répondrons dans les plus brefs délais."
  );
  contactForm.reset();
});

// Newsletter Form Submission
const newsletterForm = document.querySelector(".newsletter-form");
newsletterForm.addEventListener("submit", (e) => {
  e.preventDefault();
  // Here you would normally subscribe the user to your newsletter
  alert("Merci de vous être abonné à notre newsletter !");
  newsletterForm.reset();
});

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    if (targetId === "#") return;

    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      // Close mobile menu if open
      mobileMenu.classList.remove("active");

      // Scroll to target
      targetElement.scrollIntoView({
        behavior: "smooth"
      });
    }
  });
});

// Volume Slider Functionality
const volumeSlider = document.querySelector(".volume-slider");
const volumeLevel = document.querySelector(".volume-level");
const volumeHandle = document.querySelector(".volume-handle");

volumeSlider.addEventListener("click", (e) => {
  const sliderWidth = volumeSlider.offsetWidth;
  const clickPosition = e.offsetX;
  const percentage = (clickPosition / sliderWidth) * 100;

  // Update volume level and handle position
  volumeLevel.style.width = `${percentage}%`;
  volumeHandle.style.left = `${percentage}%`;
});

// Progress Bar Functionality
const progressContainer = document.querySelector(".progress-container");
const progressBar = document.querySelector(".progress-bar");
const progressHandle = document.querySelector(".progress-handle");

progressContainer.addEventListener("click", (e) => {
  const containerWidth = progressContainer.offsetWidth;
  const clickPosition = e.offsetX;
  const percentage = (clickPosition / containerWidth) * 100;

  // Update progress bar and handle position
  progressBar.style.width = `${percentage}%`;
  // Update time info (just for demonstration)
  updateTimeInfo(percentage);
});

function updateTimeInfo(percentage) {
  const totalSeconds = 330; // 5:30 in seconds
  const currentSeconds = Math.floor((percentage / 100) * totalSeconds);
  const currentMinutes = Math.floor(currentSeconds / 60);
  const currentRemainingSeconds = currentSeconds % 60;

  const timeInfo = document.querySelector(".time-info");
  timeInfo.textContent = `${padZero(currentMinutes)}:${padZero(
    currentRemainingSeconds
  )} / 05:30`;
}

function padZero(num) {
  return num.toString().padStart(2, "0");
}

// Header scroll effect
window.addEventListener("scroll", () => {
  const header = document.querySelector("header");
  if (window.scrollY > 100) {
    header.style.backgroundColor = "rgba(33, 33, 33, 0.95)";
    header.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.2)";
  } else {
    header.style.backgroundColor = "var(--dark-color)";
    header.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.1)";
  }
});
