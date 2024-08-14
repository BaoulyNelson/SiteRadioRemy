function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  var menuIcon = document.querySelector(".navbar-bottom .menu-icon");
  if (sidebar.classList.contains("open")) {
      sidebar.classList.remove("open");
      sidebar.classList.add("closed");
      menuIcon.classList.remove("fa-times");
      menuIcon.classList.add("fa-bars");
  } else {
      sidebar.classList.remove("closed");
      sidebar.classList.add("open");
      menuIcon.classList.remove("fa-bars");
      menuIcon.classList.add("fa-times");
  }
}