const slides = document.querySelectorAll('.slide');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const close = document.querySelector('#close');
const mainSlider = document.querySelector('#main-slider');
const plot = document.querySelector('#plot-btn');

const auto = true;
const intervalTime = 10000;
let slideInterval;

const nextSlide = () => {
    // Get current class
    const current = document.querySelector('.current');
    // Remove Class
    current.classList.remove('current');
    // Check for next slide
    if(current.nextElementSibling){
        // Add Current to next sibling
        current.nextElementSibling.classList.add('current');
    }else{
        // Add Current to start
        slides[0].classList.add('current');
    }
    setTimeout(()=>current.classList.remove('current'))
}

const prevSlide = () => {
 
    const current = document.querySelector('.current');
    
    current.classList.remove('current');
    if(current.previousElementSibling){
        current.previousElementSibling.classList.add('current');
    }else{
        slides[slides.length -1].classList.add('current');
    }
    setTimeout(()=>current.classList.remove('current'))
}

// Button Events
next.addEventListener('click', e => {
    nextSlide();
    if(auto){
        clearInterval(slides);
        slideInterval = setInterval(nextSlide, intervalTime);
    }
});
prev.addEventListener('click', e => {
    prevSlide();
    if(auto){
        clearInterval(slides);
        slideInterval = setInterval(nextSlide, intervalTime);
    }
});



// Auto Slide
if (auto){
    slideInterval = setInterval(nextSlide, intervalTime);
}


close.addEventListener('click', e => {
    mainSlider.classList.remove('active');
    // alert('closed');
});

plot.addEventListener('click', e => {
    mainSlider.classList.add('active');
    // alert('activated');
});