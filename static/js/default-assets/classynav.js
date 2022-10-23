
(function ($) {
    $.fn.classyNav = function (options) {


        var navContainer = $('.classy-nav-container');
        var classy_nav = $('.classynav ul');
        var classy_navli = $('.classynav > ul > li');
        var navbarToggler = $('.classy-navbar-toggler');
        var closeIcon = $('.classycloseIcon');
        var navToggler = $('.navbarToggler');
        var classyMenu = $('.classy-menu');
        var var_window = $(window);


        var defaultOpt = $.extend({
            theme: 'light',
            breakpoint: 991,
            openCloseSpeed: 350,
            megaopenCloseSpeed: 700,
            alwaysHidden: false,
            openMobileMenu: 'left',
            dropdownRtl: false,
            stickyNav: false,
            stickyFooterNav: false
        }, options);

        return this.each(function () {
            if (defaultOpt.theme === 'light' || defaultOpt.theme === 'dark') {
                navContainer.addClass(defaultOpt.theme);
            }
            if (defaultOpt.openMobileMenu === 'left' || defaultOpt.openMobileMenu === 'right') {
                navContainer.addClass(defaultOpt.openMobileMenu);
            }

            if (defaultOpt.dropdownRtl === true) {
                navContainer.addClass('dropdown-rtl');
            }
            navbarToggler.on('click', function () {
                navToggler.toggleClass('active');
                classyMenu.toggleClass('menu-on');
            });
            closeIcon.on('click', function () {
                classyMenu.removeClass('menu-on');
                navToggler.removeClass('active');
            });
            classy_navli.has('.dropdown').addClass('cn-dropdown-item');
            classy_navli.has('.megamenu').addClass('megamenu-item');
            classy_nav.find('li a').each(function () {
                if ($(this).next().length > 0) {
                    $(this).parent('li').addClass('has-down').append('<span class="dd-trigger"></span>');
                }
            });
            classy_nav.find('li .dd-trigger').on('click', function (e) {
                e.preventDefault();
                $(this).parent('li').children('ul').stop(true, true).slideToggle(defaultOpt.openCloseSpeed);
                $(this).parent('li').toggleClass('active');
            });
            $('.megamenu-item').removeClass('has-down');
            classy_nav.find('li .dd-trigger').on('click', function (e) {
                e.preventDefault();
                $(this).parent('li').children('.megamenu').slideToggle(defaultOpt.megaopenCloseSpeed);
            });
            function breakpointCheck() {
                var windoWidth = window.innerWidth;
                if (windoWidth <= defaultOpt.breakpoint) {
                    navContainer.removeClass('breakpoint-off').addClass('breakpoint-on');
                } else {
                    navContainer.removeClass('breakpoint-on').addClass('breakpoint-off');
                }
            }

            breakpointCheck();

            var_window.on('resize', function () {
                breakpointCheck();
            });
            if (defaultOpt.alwaysHidden === true) {
                navContainer.addClass('breakpoint-on').removeClass('breakpoint-off');
            }
            if (defaultOpt.stickyNav === true) {
                var_window.on('scroll', function () {
                    if (var_window.scrollTop() > 0) {
                        navContainer.addClass('classy-sticky');
                    } else {
                        navContainer.removeClass('classy-sticky');
                    }
                });
            }
            if (defaultOpt.stickyFooterNav === true) {
                navContainer.addClass('classy-sticky-footer');
            }
        });
    };
}(jQuery));
