function toggleSidebar() {
  console.log("toggleSidebar called"); // Debugging
  var sidebar = document.getElementById("sidebar");
  if (sidebar.style.width === "50%" || sidebar.style.width === "100%") {
      sidebar.style.width = "0";
  } else {
      sidebar.style.width = window.innerWidth <= 768 ? "100%" : "50%";
  }
}
