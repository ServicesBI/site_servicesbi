(function () {
    const storageKey = "servicesbi-theme";
    const darkTheme = "dark";

    function applyTheme(theme) {
        const isDark = theme === darkTheme;

        document.documentElement.classList.toggle("theme-dark", isDark);

        if (document.body) {
            document.body.classList.toggle("theme-dark", isDark);
        }
    }

    function getStoredTheme() {
        try {
            return localStorage.getItem(storageKey);
        } catch (error) {
            return null;
        }
    }

    function setStoredTheme(theme) {
        try {
            localStorage.setItem(storageKey, theme);
        } catch (error) {
        }
    }

    function isDarkTheme() {
        return document.documentElement.classList.contains("theme-dark");
    }

    function updateButton(button) {
        if (!button) {
            return;
        }

        const isDark = isDarkTheme();
        button.textContent = isDark ? "☾" : "☀";
        button.setAttribute(
            "aria-label",
            isDark ? "Alternar para tema claro" : "Alternar para tema escuro"
        );
    }

    applyTheme(getStoredTheme() || darkTheme);

    document.addEventListener("DOMContentLoaded", function () {
        applyTheme(getStoredTheme() || darkTheme);

        const button = document.getElementById("themeToggle");

        updateButton(button);

        if (!button) {
            return;
        }

        button.addEventListener("click", function () {
            const nextTheme = isDarkTheme() ? "light" : darkTheme;

            setStoredTheme(nextTheme);
            applyTheme(nextTheme);
            updateButton(button);
        });
    });
})();
