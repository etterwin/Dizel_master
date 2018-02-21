

$(document).ready(function () {
    $("#start").click(function () {
        var elementClick = $(this).attr("href");
        var destination = $(elementClick).offset().top;
        $('html').animate({
            scrollTop: destination }
            , 400);
        return false;
    });
});
