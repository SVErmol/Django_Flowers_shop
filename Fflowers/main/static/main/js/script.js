   $(function () {
      var Accordion = function (el, multiple) {
        this.el = el || {};
        this.multiple = multiple || false;
    
        // Variables privadas
        var links = this.el.find('.link');
        // Evento
        links.on('click', { el: this.el, multiple: this.multiple }, this.dropdown);
      };
    
      Accordion.prototype.dropdown = function (e) {
        var $el = e.data.el;
        $this = $(this),
        $next = $this.next();
    
        $next.slideToggle();
        $this.parent().toggleClass('open');
    
        if (!e.data.multiple) {
          $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
        };
      };
    
      var accordion = new Accordion($('#accordion'), false);
    });
    $(function() {
      function init() {
        $('[data-behaviour="toggle-menu-icon"]').on('click', toggleMenuIcon);
        $('[data-behaviour="toggle-link-icon"]').on('click', toggleSubMenu);
      };
      
      function toggleMenuIcon() {
        $(this).toggleClass('menu-icon--open');
        $('[data-element="toggle-nav"]').toggleClass('nav--active');
      };
      
      function toggleSubMenu() {
        $(this).toggleClass('nav__link--plus nav__link--minus');
        $('[data-behaviour="toggle-sub-menu"]').slideToggle('nav__sub-list--active');
      };
      
      init()
    });
    function viewdiv(id) {
      var el = document.getElementById(id);
      var link = document.getElementById('toggleLink');
      if (el.style.display == "block") {
        el.style.display = "none";
        link.innerText = link.getAttribute('data-text-hide');
      } else {
        el.style.display = "block";
        link.innerText = link.getAttribute('data-text-show');
      }
    }
    


    //lazy
    
    document.addEventListener("DOMContentLoaded", function() {
      var lazyloadImages = document.querySelectorAll("img.lazy");    
      var lazyloadThrottleTimeout;
      
      function lazyload () {
        if(lazyloadThrottleTimeout) {
          clearTimeout(lazyloadThrottleTimeout);
        }    
        
        lazyloadThrottleTimeout = setTimeout(function() {
            var scrollTop = window.pageYOffset;
            lazyloadImages.forEach(function(img) {
                if(img.offsetTop < (window.innerHeight + scrollTop)) {
                  img.src = img.dataset.src;
                  img.classList.remove('lazy');
                }
            });
            if(lazyloadImages.length == 0) { 
              document.removeEventListener("scroll", lazyload);
              window.removeEventListener("resize", lazyload);
              window.removeEventListener("orientationChange", lazyload);
            }
        }, 20);
      }
      
      document.addEventListener("scroll", lazyload);
      window.addEventListener("resize", lazyload);
      window.addEventListener("orientationChange", lazyload);
    });