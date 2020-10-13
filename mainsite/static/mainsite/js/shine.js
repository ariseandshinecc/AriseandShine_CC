

function ariseNavs(){
    document.getElementById('nav-small').classList.toggle('w3-show');
}



$(document).ready( function (){
    $("a").addClass("text-decoration-none");
    $("a").hover( function (){
        $(this).toggleClass("w3-hover-text-dark-blue")
    });

    $(".home-link").hover( function(){
        $(this).children("span").toggleClass("w3-hide")
    })

    $(".w3-dropdown a").click(function (){
        $(this).siblings(".dropdown-content").toggleClass("w3-show")
    })
    
})

