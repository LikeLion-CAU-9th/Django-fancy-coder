$(document).ready(function () {

    $('#itemslider').carousel({ interval: 3000 });

    $('.carousel-showmanymoveone .item').each(function () {
        var itemToClone = $(this);

        for (var i = 1; i < 6; i++) {
            itemToClone = itemToClone.next();

            if (!itemToClone.length) {
                itemToClone = $(this).siblings(':first');
            }

            itemToClone.children(':first-child').clone()
                .addClass("cloneditem-" + (i))
                .appendTo($(this));
        }
    });
    $('#itemslide').carousel({ interval: 3000 });

    $('.carousel-showmanymoveone2 .item2').each(function () {
        var itemToClone1 = $(this);

        for (var i = 1; i < 6; i++) {
            itemToClone1 = itemToClone1.next();

            if (!itemToClone1.length) {
                itemToClone1 = $(this).siblings(':first');
            }

            itemToClon1.children(':first-child').clone()
                .addClass("cloneditem2-" + (i))
                .appendTo($(this));
        }
    });
});
