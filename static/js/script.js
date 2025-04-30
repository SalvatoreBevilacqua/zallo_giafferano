/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function(){
    // Initialize Materialize components
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.modal').modal();
    $('.dropdown-trigger').dropdown({
        coverTrigger: false,
        constrainWidth: false
    });
    $('.tooltipped').tooltip();
    $('.parallax').parallax();
    $('.materialboxed').materialbox();
    
    // Auto-hide flash messages after 3 seconds
    setTimeout(function(){ 
        $('#fMessage').fadeOut(500); 
    }, 3000);
    
    // Add ripple effect to cards
    $('.card').addClass('waves-effect waves-light');
    
    // Fixes for Materialize CSS select validation
    validateMaterializeSelect();
    
    // Add smooth scrolling to page links
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        }
    });
    
    // Add animations to elements when they scroll into view
    const animatedElements = document.querySelectorAll('.card, .btn-large');
    
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated', 'fadeIn');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });
        
        animatedElements.forEach(element => {
            observer.observe(element);
        });
    }
    
    // Function to fix Materialize select validation
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        
        // Handle required selects
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ 
                "display": "block", 
                "height": "0", 
                "padding": "0", 
                "width": "0", 
                "position": "absolute" 
            });
        }
        
        // Focus in event
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            // Check select value
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                // Handle focusout for required selects
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
    
    // Password confirmation validation
    if ($('#confirm-password').length) {
        $('#confirm-password').on('keyup', function() {
            if ($(this).val() === $('#password').val()) {
                $(this).removeClass('invalid').addClass('valid');
            } else {
                $(this).removeClass('valid').addClass('invalid');
            }
        });
    }
    
    // Character counter for textareas
    $('textarea').characterCounter();
});