(function () {
  const header = document.querySelector("[data-header]");
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".site-nav");

  function setHeaderState() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 12);
  }

  function closeNav() {
    if (!toggle || !nav) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open navigation");
  }

  setHeaderState();
  window.addEventListener("scroll", setHeaderState, { passive: true });

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const isOpen = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(isOpen));
      toggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
    });

    nav.addEventListener("click", function (event) {
      if (event.target instanceof HTMLAnchorElement) {
        closeNav();
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeNav();
      }
    });
  }
})();
