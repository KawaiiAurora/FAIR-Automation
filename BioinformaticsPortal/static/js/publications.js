function togglePub(iconId){
    let icon = document.getElementById(iconId);
    icon.classList.toggle("typcn-arrow-sorted-down");
    icon.classList.toggle("typcn-arrow-sorted-up");
}

function updatePagination(currentURL, select){
    console.log("test");
    window.location.href = currentURL+"?pubs_per_page="+select.value;
}