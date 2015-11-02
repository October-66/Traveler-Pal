$(function($) {
    $('#swiper-show').swiper({
        pagination: '#swiper-show .swiper-pagination',
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: false,
        slidesPerView: 'auto',
        coverflow: {
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows: true
        }
    });

    $('#swiper-activity').swiper({
        scrollbar: '#swiper-scrollbar-activity',
        scrollbarHide: true,
        slidesPerView: 'auto',
        centeredSlides: false,
        spaceBetween: 30,
        grabCursor: true
    });

    $('#swiper-scenery').swiper({
        scrollbar: '#swiper-scrollbar-scenery',
        scrollbarHide: true,
        slidesPerView: 'auto',
        centeredSlides: false,
        spaceBetween: 30,
        grabCursor: true
    });

});
