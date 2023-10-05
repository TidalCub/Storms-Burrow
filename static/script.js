document.addEventListener('DOMContentLoaded', function() {
    var fadeIns = document.querySelectorAll('.fade-in');
    
    function fadeIn() {
      fadeIns.forEach(function(fadeIn) {
        if (isElementInViewport(fadeIn) && fadeIn.style.opacity !== "1") {
          fadeIn.style.opacity = "1";
        }
      });
    }
  
    function isElementInViewport(element) {
      var rect = element.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    }
  
    document.addEventListener('scroll', fadeIn);
    document.addEventListener('resize', fadeIn);
    fadeIn();
  });