(function () {
    "use strict";

    var STORAGE_KEY = "dm-theme";
    var ORDER = ["auto", "light", "dark"];
    var LABELS = {
        auto: "Theme: Auto",
        light: "Theme: Light",
        dark: "Theme: Dark"
    };

    function getStored() {
        try {
            var value = localStorage.getItem(STORAGE_KEY);
            if (ORDER.indexOf(value) !== -1) {
                return value;
            }
        } catch (e) {
            /* localStorage may be blocked; fall back to auto */
        }
        return "auto";
    }

    function setStored(value) {
        try {
            localStorage.setItem(STORAGE_KEY, value);
        } catch (e) {
            /* ignore */
        }
    }

    function apply(pref) {
        document.documentElement.setAttribute("data-theme", pref);
    }

    function updateButton(button, pref) {
        button.textContent = LABELS[pref];
        button.setAttribute("aria-label", LABELS[pref] + " (click to change)");
    }

    var current = getStored();
    apply(current);

    function inject() {
        var wrapper = document.querySelector(".sphinxsidebarwrapper") ||
                      document.querySelector(".sphinxsidebar");
        if (!wrapper) {
            return;
        }

        var button = document.createElement("button");
        button.id = "dm-theme-toggle";
        button.type = "button";
        updateButton(button, current);

        button.addEventListener("click", function () {
            var index = ORDER.indexOf(current);
            current = ORDER[(index + 1) % ORDER.length];
            apply(current);
            setStored(current);
            updateButton(button, current);
        });

        wrapper.insertBefore(button, wrapper.firstChild);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", inject);
    } else {
        inject();
    }
})();
