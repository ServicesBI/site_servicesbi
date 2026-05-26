(function () {
    "use strict";

    const params = new URLSearchParams(window.location.search);

    if (params.get("debugHomeText") !== "1") {
        window.ServicesBIHomeTextMetrics = {
            collect,
            print,
        };
        return;
    }

    print();

    function print() {
        const environment = getEnvironment();
        const metrics = collect();

        console.log("ServicesBI Home text metrics environment:");
        console.table([environment]);
        console.log("ServicesBI Home text metrics:");
        console.table(metrics);

        return {
            environment,
            metrics,
        };
    }

    function collect() {
        const targets = [
            {
                label: "Hero text block",
                selector: ".home-hero-copy",
            },
            {
                label: "Eyebrow SERVICESBI",
                selector: ".home-hero-copy .eyebrow",
            },
            {
                label: "Hero title",
                selector: ".home-hero-copy .section-title",
            },
            {
                label: "Hero subtitle",
                selector: ".home-hero-copy .section-subtitle",
            },
            {
                label: "Primary CTA Ver soluções",
                selector: ".home-hero-copy__actions .btn--primary",
            },
            {
                label: "Secondary CTA Falar comigo",
                selector: ".home-hero-copy__actions .btn--secondary",
            },
        ];

        return targets.map(measureTarget);
    }

    function measureTarget(target) {
        const element = document.querySelector(target.selector);

        if (!element) {
            return {
                label: target.label,
                selector: target.selector,
                error: "Element not found",
            };
        }

        const elementRect = element.getBoundingClientRect();
        const computed = window.getComputedStyle(element);
        const textMeasurement = measureFirstText(element);

        return {
            label: target.label,
            selector: target.selector,
            element_x: round(elementRect.left),
            element_y: round(elementRect.top),
            element_width: round(elementRect.width),
            element_height: round(elementRect.height),
            text_start_x: textMeasurement ? round(textMeasurement.textStart.left) : null,
            text_start_y: textMeasurement ? round(textMeasurement.textStart.top) : null,
            text_start_width: textMeasurement ? round(textMeasurement.textStart.width) : null,
            text_start_height: textMeasurement ? round(textMeasurement.textStart.height) : null,
            first_line_x: textMeasurement ? round(textMeasurement.firstLine.left) : null,
            first_line_y: textMeasurement ? round(textMeasurement.firstLine.top) : null,
            first_line_width: textMeasurement ? round(textMeasurement.firstLine.width) : null,
            first_line_height: textMeasurement ? round(textMeasurement.firstLine.height) : null,
            x_page: round(elementRect.left + window.scrollX),
            y_page: round(elementRect.top + window.scrollY),
            text_start_x_page: textMeasurement ? round(textMeasurement.textStart.left + window.scrollX) : null,
            text_start_y_page: textMeasurement ? round(textMeasurement.textStart.top + window.scrollY) : null,
            first_line_x_page: textMeasurement ? round(textMeasurement.firstLine.left + window.scrollX) : null,
            first_line_y_page: textMeasurement ? round(textMeasurement.firstLine.top + window.scrollY) : null,
            width: round(elementRect.width),
            height: round(elementRect.height),
            fontSize: computed.fontSize,
            lineHeight: computed.lineHeight,
            fontFamily: computed.fontFamily,
            fontWeight: computed.fontWeight,
            letterSpacing: computed.letterSpacing,
            textTransform: computed.textTransform,
            margin: [
                computed.marginTop,
                computed.marginRight,
                computed.marginBottom,
                computed.marginLeft,
            ].join(" "),
            padding: [
                computed.paddingTop,
                computed.paddingRight,
                computed.paddingBottom,
                computed.paddingLeft,
            ].join(" "),
            firstText: textMeasurement ? textMeasurement.textPreview : null,
            firstTextOffset: textMeasurement ? textMeasurement.textOffset : null,
        };
    }

    function measureFirstText(element) {
        const firstText = findFirstTextNode(element);

        if (!firstText) {
            return null;
        }

        const text = firstText.node.nodeValue || "";
        const firstCharRange = document.createRange();
        const firstLineRange = document.createRange();

        firstCharRange.setStart(firstText.node, firstText.offset);
        firstCharRange.setEnd(firstText.node, Math.min(firstText.offset + 1, text.length));

        firstLineRange.setStart(firstText.node, firstText.offset);
        firstLineRange.setEnd(firstText.node, text.length);

        const charRect = firstNonEmptyRect(firstCharRange);
        const lineRect = firstNonEmptyRect(firstLineRange);

        firstCharRange.detach();
        firstLineRange.detach();

        if (!charRect || !lineRect) {
            return null;
        }

        return {
            textStart: charRect,
            firstLine: lineRect,
            textPreview: text.slice(firstText.offset, firstText.offset + 80).trim(),
            textOffset: firstText.offset,
        };
    }

    function findFirstTextNode(element) {
        const walker = document.createTreeWalker(
            element,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode(node) {
                    return /\S/.test(node.nodeValue || "")
                        ? NodeFilter.FILTER_ACCEPT
                        : NodeFilter.FILTER_REJECT;
                },
            }
        );
        const node = walker.nextNode();

        if (!node) {
            return null;
        }

        const match = /\S/.exec(node.nodeValue || "");

        return {
            node,
            offset: match ? match.index : 0,
        };
    }

    function firstNonEmptyRect(range) {
        const rects = Array.from(range.getClientRects());
        const rect = rects.find((item) => item.width > 0 || item.height > 0);

        return rect || null;
    }

    function getEnvironment() {
        return {
            viewportWidth: window.innerWidth,
            viewportHeight: window.innerHeight,
            devicePixelRatio: window.devicePixelRatio,
            scrollX: window.scrollX,
            scrollY: window.scrollY,
            pathname: window.location.pathname,
            url: window.location.href,
        };
    }

    function round(value) {
        return Math.round((Number(value) + Number.EPSILON) * 1000) / 1000;
    }
})();
