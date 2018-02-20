//создать массив всех активных элементов карусели
let arr = document.querySelectorAll('.carousel__item');

//массив из картинок для вывода в центральном блоке карусели, всегда 9 штук
let arrImages = ['assets/pictures/png/photo-1.jpg',
    'assets/pictures/png/photo-2.jpg',
    'assets/pictures/png/photo-3.JPG',
    'assets/pictures/png/photo-4.jpg',
    'assets/pictures/png/photo-1.jpg',
    'assets/pictures/png/photo-2.jpg',
    'assets/pictures/png/photo-3.JPG',
    'assets/pictures/png/photo-4.jpg',
    'assets/pictures/png/photo-1.jpg'];

//проверка
console.log(arr.length);
console.log(arrImages.length);

//замена картинки
function carouselChange() {
    for(let i = 0; i < arr.length - 1 ; i++) {
        for(let j = 0; j < arrImages.length; j++) {
            if (i === j) {
                //изменяем атрибут центральной картинки
                document.getElementById('carousel-img').setAttribute('src', arrImages[j]);
            }
            else {
                return true;
            }
        }
    }
}

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
