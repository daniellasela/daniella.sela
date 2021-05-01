function onClick(e) {
  lastClicked.parentElement.classList.remove("active");
  e.target.parentElement.classList.add("active");
  lastClicked = e.target;
}

let about_div = document.getElementById("about_div");
let lastClicked = about_div;
about_div.addEventListener("click", onClick);

let education_div = document.getElementById("education_div");
education_div.addEventListener("click", onClick);

let works_div = document.getElementById("works_div");
works_div.addEventListener("click", onClick);

let army_div = document.getElementById("army_div");
army_div.addEventListener("click", onClick);

let contact_div = document.getElementById("contact_div");
contact_div.addEventListener("click", onClick);
