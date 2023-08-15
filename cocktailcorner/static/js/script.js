document.addEventListener('DOMContentLoaded', function () {
    // Initialize mobile sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Initialize form select list
    let selectlist = document.querySelectorAll('select');
    M.FormSelect.init(selectlist);
});


    
