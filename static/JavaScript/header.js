document.addEventListener("DOMContentLoaded", function () {
  let lastScrollTop = 0;
  const header = document.querySelector(".header-container");

  function handleScroll() {
    const isMobile = window.innerWidth <= 768;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (isMobile && header) {
      if (scrollTop - lastScrollTop > 10) {
        header.classList.add("hide-on-scroll");
      } else if (lastScrollTop - scrollTop > 2) {
        header.classList.remove("hide-on-scroll");
      }
      lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    } else if (header) {
      header.classList.remove("hide-on-scroll");
    }
  }

  window.addEventListener("scroll", handleScroll);
});

document.addEventListener("DOMContentLoaded", function () {
  const moreBtn = document.getElementById("moreBtn");
  const navList = document.getElementById("navList");

  moreBtn.addEventListener("click", function () {
    navList.classList.toggle("show");
    moreBtn.classList.toggle("open");
  });
});


