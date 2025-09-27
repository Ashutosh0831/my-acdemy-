document.addEventListener("DOMContentLoaded", function () {
  const moreText = document.getElementById("more");
  const btnText = document.getElementById("toggleBtn");

  function toggleMenu() {
    if (window.innerWidth <= 768) {
      moreText.classList.toggle("show");
    }
  }

  function resetMenuOnResize() {
    if (window.innerWidth > 768) {
      moreText.classList.remove("show");
    }
  }

  btnText.addEventListener("click", toggleMenu);
  window.addEventListener("resize", resetMenuOnResize);
});