document.getElementById('searchIcon').addEventListener('click', function() {
    var form = document.getElementById('searchForm');
    var searchInput = form.querySelector('input[name="q"]');
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
        searchInput.focus();
    } else {
        form.style.display = 'none';
    }
});