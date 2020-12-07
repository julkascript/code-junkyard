let pass1 = document.getElementById("pass1")
let pass2 = document.getElementById("pass2")
let passCheck = document.getElementById("pass-check")
let matchCase = document.getElementById("match-case")
let lengthCase = document.getElementById("length-case")
let lowerCase = document.getElementById("lower-case")
let upperCase = document.getElementById("upper-case")


function hasLowerCase(str) {
    return (/[a-z]/.test(str));
}

function hasUpperCase(str) {
    return (/[A-Z]/.test(str));
}

function checker() {
    passCheck.style.display = "block";
    if (pass1.value !== "" && pass2.value !== "") {
        if (pass1.value !== pass2.value) {
            pass1.style.borderColor = "red";
            pass2.style.borderColor = "red";
            matchCase.style.color = "red";
        }
        if (pass1.value === pass2.value) {
            pass1.style.borderColor = "green";
            pass2.style.borderColor = "green";
            matchCase.style.color = "green";
        }
        if (pass1.value.length < 8) {
            lengthCase.style.color = "red";
        }
        if (pass1.value.length >= 8) {
            lengthCase.style.color = "green";
        }
        if (hasLowerCase(pass1.value)) {
            lowerCase.style.color = "green";
        }
        if (!hasLowerCase(pass1.value)) {
            lowerCase.style.color = "red";
        }
        if (hasUpperCase(pass1.value)) {
            upperCase.style.color = "green";
        }
        if (!hasUpperCase(pass1.value)) {
            upperCase.style.color = "red";
        }
    }
}

pass1.addEventListener("keyup", checker)
pass2.addEventListener("keyup", checker)