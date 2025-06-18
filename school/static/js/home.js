// Initialize Swiper
const swiper = new Swiper(".swiper", {
    loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    keyboard: {
        enabled: true,
        onlyInViewport: true,
    },
    effect: "fade",
    fadeEffect: {
        crossFade: true,
    },
}); 