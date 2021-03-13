function togglePub(iconId){
    let icon = document.getElementById(iconId);
    icon.classList.toggle("typcn-arrow-sorted-down");
    icon.classList.toggle("typcn-arrow-sorted-up");
}

function updatePagination(currentURL, select){
    window.location.href = currentURL+"?pubs_per_page="+select.value;
}