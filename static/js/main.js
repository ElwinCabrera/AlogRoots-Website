$(document).ready(documentReady);


function documentReady(jQuery) {

    $(".sidebar>ul>li div[data-toggle='collapse']").click(onSidebarClickEvent);

    $('[data-spy="scroll"]').on('activate.bs.scrollspy', function() {
        console.log("here");
    });

}


/* Events  Handlers*/
function onSidebarClickEvent(event) {
    console.log("A section on the sidebar was clicked");
    //console.log(this);
    //console.log(event.target);

    var arrowIcon = $(this).find("i");

    if ($(this).attr("aria-expanded") === "false") {
        arrowIcon.removeClass("fa-angle-down");
        arrowIcon.addClass("fa-angle-up");
    } else {
        arrowIcon.removeClass("fa-angle-up");
        arrowIcon.addClass("fa-angle-down");
    }
}