document.getElementById('togglePanel').addEventListener('click', function() {
    var sidePanel = document.getElementById('sidePanel');
    if (sidePanel.style.left === '0px') {
      sidePanel.style.left = '-250px';
      document.getElementById('togglePanel').innerHTML = '&#9776;';
    } else {
      sidePanel.style.left = '0';
      document.getElementById('togglePanel').innerHTML = '&times;';
    }
  });
  
  document.getElementById('closeButton').addEventListener('click', function() {
    var sidePanel = document.getElementById('sidePanel');
    sidePanel.style.left = '-250px';
    document.getElementById('togglePanel').innerHTML = '&#9776;';
  });
  
  $('#customSwitch').change(function() {
    if ($(this).is(':checked')) {
      $('body').addClass('dark-mode');
    } else {
      $('body').removeClass('dark-mode');
    }
  });
  