(function () {
    const viewerHost = document.getElementById("homeRobotViewer");

    if (!viewerHost) {
        return;
    }

    const sceneUrl = viewerHost.dataset.sceneUrl;
    const loader = viewerHost.querySelector(".home-robot__loader");

    if (!sceneUrl) {
        viewerHost.classList.add("is-loaded");
        return;
    }

    function hideLoader() {
        viewerHost.classList.add("is-loaded");

        if (loader) {
            loader.setAttribute("aria-hidden", "true");
        }
    }

    const viewer = document.createElement("spline-viewer");

    viewer.setAttribute("url", sceneUrl);
    viewer.setAttribute("loading-anim-type", "none");
    viewer.style.width = "100%";
    viewer.style.height = "100%";
    viewer.style.display = "block";
    viewer.style.background = "transparent";

    viewer.addEventListener("load", hideLoader, { once: true });
    viewer.addEventListener("load-complete", hideLoader, { once: true });

    viewerHost.appendChild(viewer);
    window.setTimeout(hideLoader, 3500);
})();
