(function () {
    "use strict";

    var SHOW_AFTER = 300;
    var button = null;
    var scheduled = false;

    function prefersReducedMotion() {
        return window.matchMedia &&
            window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    }

    function updateVisibility() {
        scheduled = false;
        if (!button) {
            return;
        }
        if (window.scrollY > SHOW_AFTER) {
            button.classList.add("is-visible");
        } else {
            button.classList.remove("is-visible");
        }
    }

    function onScroll() {
        if (scheduled) {
            return;
        }
        scheduled = true;
        window.requestAnimationFrame(updateVisibility);
    }

    function scrollToTop() {
        if (prefersReducedMotion()) {
            window.scrollTo(0, 0);
            return;
        }
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function createButton() {
        button = document.createElement("button");
        button.id = "dm-back-to-top";
        button.type = "button";
        button.setAttribute("aria-label", "Back to top");
        button.setAttribute("title", "Back to top");
        button.innerHTML =
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" ' +
            'fill="none" stroke="currentColor" stroke-width="2" ' +
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
            '<polyline points="6 15 12 9 18 15"></polyline>' +
            "</svg>";
        button.addEventListener("click", scrollToTop);
        document.body.appendChild(button);
        updateVisibility();
    }

    function init() {
        createButton();
        window.addEventListener("scroll", onScroll, { passive: true });
        window.addEventListener("resize", onScroll, { passive: true });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
