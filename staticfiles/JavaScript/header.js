document.addEventListener("DOMContentLoaded", function () {
  // Hide header on scroll (mobile)
  let lastScrollTop = 0;
  const header = document.querySelector(".header-container");
  window.addEventListener("scroll", function () {
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
  });

  // Toggle nav links on mobile
  const navLinks = document.getElementById("navLinks");
  const toggleBtn = document.getElementById("toggleBtn");
  toggleBtn.addEventListener("click", function () {
    if (window.innerWidth <= 768) {
      navLinks.classList.toggle("show");
    }
  });
  window.addEventListener("resize", function () {
    if (window.innerWidth > 768) {
      navLinks.classList.remove("show");
    }
  });
});