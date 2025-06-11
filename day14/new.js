console.log("JS file created");
console.log("div");

const doc = document.getElementsByTagName("div")
let div = doc[0];
div.textContent = "All of us are dead"

let tryDiv = document.getElementById("try")

tryDiv.style.backgroundColor = "plum"
tryDiv.style.border = "2px solid black"

tryDiv.textContent = "try"
console.log(tryDiv)