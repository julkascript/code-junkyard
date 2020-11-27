let scrollBtn = document.getElementById('scroll-btn')
scrollBtn.addEventListener("click", () => {
// Scroll to a certain element
    document.querySelector('.carousel-indicators').scrollIntoView({
        behavior: 'smooth'
    });
})

let signUpBtn = document.getElementById('sign-up-btn')
signUpBtn.addEventListener("click", function () {
    console.log(222)
    let pass1 = document.getElementById('pass1')
    let pass2 = document.getElementById('pass2')
    if (pass1.value !== pass2.value){
        pass1.style.border = '1px solid red';
        pass2.style.border = '1px solid red';
    }
    else {
        pass1.style.border = 'none';
        pass2.style.border = 'none';
    }

})
