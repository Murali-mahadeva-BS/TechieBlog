$(document).ready(function() {
    // show the alert
    setTimeout(function() {
        $(".alert").alert('close');
    }, 4000);
});

$(document).ready(function() {
  //initializing tooltip
  $('[data-toggle="tooltip"]').tooltip();
});