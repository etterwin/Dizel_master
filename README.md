# Дизель МАСТЕР
**Ленд для компании по ремонту и обслуживанию в Поволжье (г. Нижний Новгород)**

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

~~Это должно было стать тестовым заданием, но не вышло~~

**Несложный ленд, наделенный следующими особенностями:**
1. Три формы обратной связи, а именно: имя+телефон, название детали+телефон, вопрос+телефон.
2. Постоянно спамящий попап, куда бы вы не ткнули, например, на всплывающее меню авто. Попап предлагает связаться с диллером (не реализовано).
3. В футере интерактивная Яндекс карта, что мне кажется очень не юзабельным.
4. В меру анимации (мигание фар при наведении на машину, анимация прогресса от сломанной машины к починенной).
5. Каруселька для десктопных устройств, разбитая на 10 элементов, где в десятом выводится объект элемента (с 1 по 9), на который вы кликнули.
6. Прокрутка до карты и первой формы на ленде.

Для реализации я использовала **Python**, **Django**, **jQuery** и **SASS(scss)**. Бэкенд полностью написан на **Django**, прокрутка на **jQuery**. Карусель не удалось написать, т.к. я не смогла сделать этого силами дефолтного **JS** или **jQuery**, однако я знаю способ на **Vue.js**, который не работает в паре с Django.

В целом хочется отметить, что это был интересный опыт, хоть я не довела проект до конца и слилась по причине несоответсвия технологий с заказчиком. Почему это нельзя было выяснить раньше - никто не знает.

**Что нужно было реализовать, но я не сделала этого:**
1. Создание **"мульти"-ленда** через **utm-метки**.
<br/>*Дана таблица, содержащая  6 колонок, каждая содержит пару "ключ-значение". Необходимо брать данные "ключа" для метки и выводить его "значение" в объекте на странице, а именно изменять текст в трех местах на ленде.*
2. Отправка форм на email представителя компании.
3. Карусель. 
<br/>*Возможно, картинки стоило отдвать через views.py?*
4. Доделанный адаптив. 
<br/>*Пункт не готов по причине отсутсвия необходимых мне ассетов и текста для наполнения. Ленд содержит очень много абсолютных объектов.*

<hr/>

По итогу, я отказалась от выполнения дальнейших работ, т.к. ленд попросили перенести на **PHP**. Я вернула всю статику, предварительно подредактировав ее.
