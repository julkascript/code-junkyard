let scrollBtn = document.getElementById('scroll-btn')
scrollBtn.addEventListener("click", () => {
// Scroll to a certain element
    document.querySelector('.carousel-indicators').scrollIntoView({
        behavior: 'smooth'
    });
})

// // updated 2019
// const input = document.getElementById("search-input");
// const searchBtn = document.getElementById("search-btn");
//
// const expand = () => {
//   searchBtn.classList.toggle("close");
//   input.classList.toggle("square");
// };
//
// searchBtn.addEventListener("click", expand);
