/**
 * Author: Elwin Cabrera - 2019
 * 
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 * 
 * Please consider sharing any cool additons to this project! :)
 */
$(document).ready(documentReady);


function documentReady(jQuery) {
    console.log("main.js ready!");
    $(window).scroll(scrollEvent);

    $(".sidebar>ul>li div[data-toggle='collapse']").click(onSidebarClickEvent);
    $('.solution-btn').click(solutionsBtnClick);

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

function solutionsBtnClick(event) {

    if ($(this).text() === "Show Solutions") {
        $(this).text("Hide Solutions");
    } else {
        $(this).text("Show Solutions");
    }
}

function scrollEvent(event) {
    var scroll = $(window).scrollTop();



    $('.toc-item a.active').removeClass('active');
    console.log("scroll is: " + scroll + " runtime is: " + $('#run-time').offset().top);

    $('.article-sec').each(function(_, section) {
        var secId = section.id;

        if ($(section).offset().top < scroll + 10) {
            $('.toc-item a.active').removeClass('active');
            $('.toc-item a[href=\'#' + secId + '\']').addClass('active');

        }
    });
}