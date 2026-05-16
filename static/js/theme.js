(function () {
    const storageKey = "servicesbi-theme";
    const darkTheme = "dark";

    function applyTheme(theme) {
        document.body.classList.toggle("theme-dark", theme === darkTheme);
    }

    function updateButton(button) {
        if (!button) {
            return;
        }

        const isDark = document.body.classList.contains("theme-dark");
        button.textContent = isDark ? "☾" : "☀";
        button.setAttribute(
            "aria-label",
            isDark ? "Alternar para tema claro" : "Alternar para tema escuro"
        );
    }

    applyTheme(localStorage.getItem(storageKey));

    document.addEventListener("DOMContentLoaded", function () {
        const button = document.getElementById("themeToggle");

        updateButton(button);

        if (!button) {
            return;
        }

        button.addEventListener("click", function () {
            const nextTheme = document.body.classList.contains("theme-dark") ? "light" : darkTheme;

            localStorage.setItem(storageKey, nextTheme);
            applyTheme(nextTheme);
            updateButton(button);
        });
    });
})();
