(function () {
    const viewerHost = document.getElementById("homeRobotViewer");
    if (!viewerHost) return;

    const loader = viewerHost.querySelector(".home-robot__loader");
    const iframe = viewerHost.querySelector(".home-robot__iframe");

    function hideLoader() {
        viewerHost.classList.add("is-loaded");
        if (loader) loader.setAttribute("aria-hidden", "true");
    }

    if (iframe) {
        iframe.addEventListener("load", hideLoader, { once: true });
    }

    // Timeout de segurança: esconde o loader mesmo se o iframe demorar ou falhar
    window.setTimeout(hideLoader, 8000);
})();
