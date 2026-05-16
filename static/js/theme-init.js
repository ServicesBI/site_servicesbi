(function () {
    const storageKey = "servicesbi-theme";

    try {
        const theme = localStorage.getItem(storageKey);
        document.documentElement.classList.toggle("theme-dark", theme === "dark");
    } catch (error) {
        document.documentElement.classList.remove("theme-dark");
    }
})();
