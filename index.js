const swiper = new Swiper('.slider-wrapper', {
    grabCursor:true,
    loop: true,
    spaceBetween:30,
  
    pagination: {
      el: '.swiper-pagination',
      clickable:true,
      dynamicBullets:true
    },
  
  
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        0: { 
            slidesPerView: 1,
           
        },
        768: { 
            slidesPerView: 2,
           
        },
        1024: { 
            slidesPerView: 3,
            
        }
    }
   
  });
  var images=['./images/city1.jpeg' , './images/city2.jpg', './images/city3.jpg'];
  var index=0;
  function switchimages() {
    index=(index +1)% images.length;
    document.getElementById("slide-img").src=images[index];
  }
  setInterval(switchimages,5000)
  

  document.addEventListener("click",showslidebar)
  function showslidebar() {
    const slidebar=document.getElementsByClassName("slide")
    slidebar.classList.add('show');
  }