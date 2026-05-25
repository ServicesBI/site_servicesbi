(function () {
    const STORAGE_KEY = "servicesbi-theme";
    const SESSION_KEY = "servicesbi-theme-session-started";

    try {
        const hasSessionStarted = sessionStorage.getItem(SESSION_KEY) === "1";

        if (!hasSessionStarted) {
            document.documentElement.classList.add("theme-dark");
            localStorage.setItem(STORAGE_KEY, "dark");
            sessionStorage.setItem(SESSION_KEY, "1");
        } else {
            const savedTheme = localStorage.getItem(STORAGE_KEY);
            const isDark = savedTheme !== "light";
            document.documentElement.classList.toggle("theme-dark", isDark);

            if (savedTheme !== "light" && savedTheme !== "dark") {
                localStorage.setItem(STORAGE_KEY, "dark");
            }
        }
    } catch (error) {
        document.documentElement.classList.add("theme-dark");
    }
})();
