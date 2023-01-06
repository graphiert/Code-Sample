const toggleNav = document.querySelector(".menu-toggle input");
const navUl = document.querySelector("nav ul");
    
window.onclick = e => {
  if (
    e.target != toggleNav &&
    e.target != navUl &&
    window.innerWidth < 576
  ) {
    toggleNav.checked = false;
    navUl.style.display = 'none';
  }
};
    
toggleNav.onclick = () => {
  toggleNav.checked ?
    navUl.style.display = "flex" :
    navUl.style.display = "none";
};
