(() => {
    const portfolio = document.querySelector(".home-portfolio");

    if (!portfolio) {
        return;
    }

    const filters = [...portfolio.querySelectorAll(".home-portfolio__filter")];
    const cards = [...portfolio.querySelectorAll(".home-portfolio-card")];

    const applyFilter = (filter) => {
        filters.forEach((button) => {
            const isActive = button.dataset.filter === filter;
            button.classList.toggle("is-active", isActive);
            button.setAttribute("aria-selected", String(isActive));
        });

        cards.forEach((card) => {
            const categories = (card.dataset.category || "").split(" ");
            card.classList.toggle("is-hidden", !categories.includes(filter));
        });
    };

    filters.forEach((button) => {
        button.addEventListener("click", () => {
            applyFilter(button.dataset.filter);
        });
    });
})();
