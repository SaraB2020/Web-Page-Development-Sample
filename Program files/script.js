var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}
//checkout add shadow with javascript
//function boxShadow(){
function boxShadow() {
  document.getElementById("navbar").style.boxShadow = "0px 20px 30px black";
}
//Scrolling function
window.onscroll = function() {myScroll()};
function myScroll() {
  if (document.body.scrollTop > 330 || document.documentElement.scrollTop > 330) {
    document.getElementById("navbar").style.boxShadow ="0px 20px 30px black";
    document.getElementById("navbar").style.transition ="1s ease";
  } else {
    document.getElementById("navbar").style.boxShadow = "none";
  }
}
