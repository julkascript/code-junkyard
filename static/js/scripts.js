let scrollBtn = document.getElementById('scroll-btn')
scrollBtn.addEventListener("click", () => {
// Scroll to a certain element
    document.querySelector('.carousel-indicators').scrollIntoView({
        behavior: 'smooth'
    });
})


