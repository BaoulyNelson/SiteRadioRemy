function toggleMenu() {
    var menuIcon = document.getElementById('menu-icon');
    var crossIcon = document.getElementById('cross-icon');
    var menuList = document.getElementById('menu-list');

    menuList.classList.toggle('show-menu');
    menuIcon.classList.toggle('cross-icon');
    crossIcon.classList.toggle('cross-icon');
}
