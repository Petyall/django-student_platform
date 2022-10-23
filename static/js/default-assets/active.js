(function ($) {
    'use strict';

    var uza_window = $(window);
    if ($.fn.classyNav) {
        $('#uzaNav').classyNav();
    }
    if ($.fn.owlCarousel) {
        var welcomeSlider = $('.welcome-slides');
        welcomeSlider.owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            smartSpeed: 1500,
            animateIn: 'fadeIn',
            animateOut: 'fadeOut',
            autoplayTimeout: 7000,
            nav: false
        })
        welcomeSlider.on('translate.owl.carousel', function () {
            var layer = $("[data-animation]");
            layer.each(function () {
                var anim_name = $(this).data('animation');
                $(this).removeClass('animated ' + anim_name).css('opacity', '0');
            });
        });
        $("[data-delay]").each(function () {
            var anim_del = $(this).data('delay');
            $(this).css('animation-delay', anim_del);
        });
        $("[data-duration]").each(function () {
            var anim_dur = $(this).data('duration');
            $(this).css('animation-duration', anim_dur);
        });
        welcomeSlider.on('translated.owl.carousel', function () {
            var layer = welcomeSlider.find('.owl-item.active').find("[data-animation]");
            layer.each(function () {
                var anim_name = $(this).data('animation');
                $(this).addClass('animated ' + anim_name).css('opacity', '1');
            });
        });
    }
    if ($.fn.owlCarousel) {
        var portfolioSlide = $('.portfolio-sildes');
        portfolioSlide.owlCarousel({
            items: 4,
            margin: 50,
            loop: true,
            autoplay: true,
            smartSpeed: 1500,
            dots: true,
            responsive: {
                0: {
                    items: 1
                },
                576: {
                    items: 2
                },
                992: {
                    items: 3
                },
                1400: {
                    items: 4
                }
            }
        });
    }
    if ($.fn.owlCarousel) {
        var testimonialSlide = $('.testimonial-slides');
        testimonialSlide.owlCarousel({
            items: 1,
            margin: 0,
            loop: true,
            autoplay: true,
            autoplayTimeout: 10000,
            smartSpeed: 1500,
            nav: true,
            navText: ['<i class="arrow_carrot-left"></i>', '<i class="arrow_carrot-right"></i>']
        });
    }
    if ($.fn.owlCarousel) {
        var teamSlide = $('.team-sildes');
        teamSlide.owlCarousel({
            items: 4,
            margin: 50,
            loop: true,
            autoplay: true,
            smartSpeed: 1500,
            dots: true,
            responsive: {
                0: {
                    items: 1
                },
                576: {
                    items: 2
                },
                992: {
                    items: 3
                },
                1400: {
                    items: 4
                }
            }
        });
    }
    if ($.fn.imagesLoaded) {
        $('.uza-portfolio').imagesLoaded(function () {
            $('.portfolio-menu').on('click', 'button', function () {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({
                    filter: filterValue
                });
            });
            var $grid = $('.uza-portfolio').isotope({
                itemSelector: '.single-portfolio-item',
                percentPosition: true,
                masonry: {
                    columnWidth: '.single-portfolio-item'
                }
            });
        });
    }








    $('.portfolio-menu button.btn').on('click', function () {
        $('.portfolio-menu button.btn').removeClass('active');
        $(this).addClass('active');
    })




    if ($.fn.tooltip) {
        $('[data-toggle="tooltip"]').tooltip();
    }


    if (uza_window.width() > 767) {
        new WOW().init();
    }


    if ($.fn.jarallax) {
        $('.jarallax').jarallax({
            speed: 0.2
        });
    }

    if ($.fn.scrollUp) {
        uza_window.scrollUp({
            scrollSpeed: 2000,
            scrollText: '<i class="fa fa-angle-up"</i>'
        });
    }

    uza_window.on('scroll', function () {
        if (uza_window.scrollTop() > 0) {
            $('.main-header-area').addClass('sticky');
        } else {
            $('.main-header-area').removeClass('sticky');
        }
    });


    if ($.fn.counterUp) {
        $('.counter').counterUp({
            delay: 15,
            time: 1500
        });
    }


    $('a[href="#"]').click(function ($) {
        $.preventDefault();
    });

})(jQuery);