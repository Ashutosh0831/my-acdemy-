document.addEventListener("DOMContentLoaded", function () {
  const moreBtn = document.getElementById("moreBtn");
  const navList = document.getElementById("navList");

  moreBtn.addEventListener("click", function () {
    navList.classList.toggle("show");
    moreBtn.classList.toggle("open");
  });
});
