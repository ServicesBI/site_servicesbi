/* ServicesBI — Hero: sequência Dados → Organização → Indicadores → Decisão.
   Telas largas e altas o bastante: o hero fica fixo e as etapas seguem a rolagem.
   Celular, telas baixas: as etapas avançam sozinhas quando o painel aparece.
   Sem JS ou com movimento reduzido: o painel fica completo (etapa 4). */
(function () {
    var hero = document.getElementById("hvHero");
    var story = document.getElementById("hvStory");
    if (!hero || !story) return;

    var STEPS = 4;
    var STORY_LEN = 2400;         // px de rolagem para percorrer as 4 etapas (~600 px por etapa)
    var STEP_HOLD = 650;          // ms mínimos em cada etapa: rolagem rápida avança uma etapa por vez
    var AUTO_MS = 2300;           // tempo por etapa no modo automático
    var tabs = Array.prototype.slice.call(story.querySelectorAll(".hv-story__tab"));
    var fills = tabs.map(function (t) { return t.querySelector(".hv-story__fill"); });
    var header = document.querySelector(".site-header") || document.querySelector("header");
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var mode = null, timer = null, autoDone = false, ticking = false;

    var current = 0;
    var kpis = Array.prototype.slice.call(story.querySelectorAll(".hv-kpi__v[data-n]"));
    function countUp() {           // indicadores contam de 0 até o valor ao entrar em "Indicadores"
        kpis.forEach(function (el) {
            var alvo = parseFloat(el.getAttribute("data-n")), suf = el.getAttribute("data-suf") || "", t0 = null;
            function frame(t) {
                if (t0 === null) t0 = t;
                var p = Math.min(1, (t - t0) / 900), v = alvo * (1 - Math.pow(1 - p, 3));
                el.textContent = v.toFixed(1).replace(".", ",") + suf;
                if (p < 1) requestAnimationFrame(frame);
            }
            requestAnimationFrame(frame);
        });
    }

    /* ---------- Decisão: simulador de saídas para o caixa ---------- */
    var dec = (function () {
        var pane = document.getElementById("hvDecisao");
        var dadosEl = document.getElementById("hvDecisaoDados");
        if (!pane || !dadosEl) return null;
        var d = JSON.parse(dadosEl.textContent);
        var cols = Array.prototype.slice.call(pane.querySelectorAll(".hv-dec__col"));
        var opts = Array.prototype.slice.call(pane.querySelectorAll(".hv-dec__opt"));
        var res = {
            menor: pane.querySelector('[data-res="menor"]'),
            semanas: pane.querySelector('[data-res="semanas"]'),
            custo: pane.querySelector('[data-res="custo"]')
        };
        var porId = {};
        d.opcoes.forEach(function (o) { porId[o.id] = o; });
        var ligadas = {}, mexeu = false, autoTimer = null;
        var fmt = function (n) { return (Math.round(n * 10) / 10).toLocaleString("pt-BR"); };
        var baseMenor = Math.min.apply(null, d.semanas);
        var baseAbaixo = d.semanas.filter(function (v) { return v < d.minimo; }).length;
        var semanaAlerta = d.semanas.findIndex(function (v) { return v < d.minimo; });

        function render() {
            var ids = Object.keys(ligadas).filter(function (k) { return ligadas[k]; });
            var vals = d.semanas.map(function (v, i) {
                return ids.reduce(function (s, id) { return s + (porId[id].efeito[String(i + 1)] || 0); }, v);
            });
            vals.forEach(function (v, i) {
                var bar = cols[i].querySelector(".hv-dec__bar"), em = cols[i].querySelector(".hv-dec__delta");
                var pct = v / d.escala * 100, delta = v - d.semanas[i];
                bar.style.height = pct + "%";
                bar.classList.toggle("is-low", v < d.minimo);
                bar.classList.toggle("is-up", v >= d.minimo && delta > 0.5);
                em.textContent = delta > 0.5 ? "+" + fmt(delta) : "";
                em.style.bottom = "calc(" + pct + "% + 3px)";
                em.classList.toggle("is-on", delta > 0.5 && i === semanaAlerta);
            });
            var menor = Math.min.apply(null, vals);
            var abaixo = vals.filter(function (v) { return v < d.minimo; }).length;
            var custo = ids.reduce(function (s, id) { return s + porId[id].custo; }, 0);
            var mudou = ids.length > 0;
            res.menor.innerHTML = (mudou ? "<s>" + fmt(baseMenor) + "</s>" : "") + "R$ " + fmt(menor) + " mil";
            res.menor.className = "hv-dec__v " + (menor < d.minimo ? "is-bad" : "is-good");
            res.semanas.innerHTML = (mudou ? "<s>" + baseAbaixo + "</s>" : "") + abaixo;
            res.semanas.className = "hv-dec__v " + (abaixo ? "is-bad" : "is-good");
            res.custo.textContent = custo ? "R$ " + fmt(custo) + " mil" : "R$ 0";
            opts.forEach(function (o) { o.setAttribute("aria-checked", ligadas[o.getAttribute("data-opcao")] ? "true" : "false"); });
            story.classList.toggle("hv-dec--ok", abaixo === 0);
        }
        opts.forEach(function (o) {
            o.addEventListener("click", function () {
                mexeu = true;
                clearTimeout(autoTimer);
                var id = o.getAttribute("data-opcao");
                ligadas[id] = !ligadas[id];
                render();
            });
        });
        render();
        return {
            entrar: function () {           // ao chegar em "Decisão": liga a recomendada se o visitante ainda não mexeu
                if (mexeu) return;
                clearTimeout(autoTimer);
                var rec = pane.querySelector('[data-recomendado="1"]');
                if (!rec) return;
                autoTimer = setTimeout(function () {
                    ligadas[rec.getAttribute("data-opcao")] = true;
                    render();
                }, reduce ? 0 : 1500);
            },
            sair: function () {             // voltou para trás sem mexer: reinicia para a cena repetir
                clearTimeout(autoTimer);
                if (mexeu) return;
                ligadas = {};
                render();
            }
        };
    })();

    function setStep(n) {
        if (n === current) return;
        if (n >= 3 && current < 3 && current !== 0 && !reduce) countUp();
        if (dec) { if (n === 4) dec.entrar(); else if (current === 4) dec.sair(); }
        current = n;
        story.setAttribute("data-step", String(n));
        tabs.forEach(function (t, i) {
            t.classList.toggle("is-on", i < n);
            if (i === n - 1) t.setAttribute("aria-current", "step"); else t.removeAttribute("aria-current");
        });
    }
    function setFills(p) {          // p de 0 a 1 ao longo das 4 etapas
        fills.forEach(function (f, i) {
            var v = Math.min(1, Math.max(0, p * STEPS - i));
            f.style.transition = "none";
            f.style.width = (v * 100) + "%";
        });
    }

    function hdr() { return header ? header.offsetHeight : 0; }

    function onScroll() {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
            ticking = false;
            if (mode !== "pin") return;
            var top = hero.getBoundingClientRect().top;
            var p = Math.min(1, Math.max(0, (hdr() - top) / STORY_LEN));
            target = Math.min(STEPS, Math.floor(p * STEPS) + 1);
            setFills(p);
            advance();
        });
    }

    /* Segura cada etapa um tempinho: se a rolagem pular da 1 para a 4,
       as etapas passam uma a uma (1 → 2 → 3 → 4), com STEP_HOLD entre elas. */
    var target = 1, lastChange = 0, holdTimer = null;
    function advance() {
        if (holdTimer || current === target) return;
        var espera = STEP_HOLD - (Date.now() - lastChange);
        if (current === 0 || espera <= 0) {
            setStep(current === 0 ? target : current + (target > current ? 1 : -1));
            lastChange = Date.now();
            if (current !== target) holdTimer = setTimeout(function () { holdTimer = null; advance(); }, STEP_HOLD);
        } else {
            holdTimer = setTimeout(function () { holdTimer = null; advance(); }, espera);
        }
    }

    function stopAuto() { if (timer) { clearTimeout(timer); timer = null; } }
    function runAuto(n) {
        setStep(n);
        fills.forEach(function (f, i) {
            if (i < n - 1) { f.style.transition = "none"; f.style.width = "100%"; }
            else if (i === n - 1) {
                f.style.transition = "none"; f.style.width = "0%";
                void f.offsetWidth;
                f.style.transition = "width " + AUTO_MS + "ms linear";
                f.style.width = "100%";
            } else { f.style.transition = "none"; f.style.width = "0%"; }
        });
        if (n < STEPS) timer = setTimeout(function () { runAuto(n + 1); }, AUTO_MS);
        else autoDone = true;
    }
    var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
            if (mode === "auto" && e.isIntersecting && !autoDone && !timer) runAuto(1);
        });
    }, { threshold: 0.3 }) : null;

    function layout() {
        stopAuto();
        hero.classList.remove("is-pinned");
        hero.style.removeProperty("--pin-h");
        if (reduce) { mode = "static"; setStep(STEPS); setFills(1); return; }

        var h = hdr();
        var pinH = window.innerHeight - h;
        var grid = hero.querySelector(".hv-hero__grid");
        var wide = window.matchMedia("(min-width: 1000px)").matches;
        hero.classList.add("is-pinned");                 // mede já com o padding reduzido
        hero.style.setProperty("--hdr", h + "px");
        hero.style.setProperty("--pin-h", pinH + "px");
        hero.style.setProperty("--story-len", STORY_LEN + "px");
        var fits = wide && grid.offsetHeight <= pinH;
        if (fits) {
            mode = "pin";
            onScroll();
        } else {
            hero.classList.remove("is-pinned");
            mode = "auto";
            if (autoDone) { setStep(STEPS); setFills(1); }
            else {
                setStep(1); setFills(0);
                // unobserve + observe: o observador reavalia na hora; se o painel
                // já estiver na tela, a sequência recomeça em vez de ficar parada.
                if (io) { io.unobserve(story); io.observe(story); } else runAuto(1);
            }
        }
    }

    Array.prototype.slice.call(story.querySelectorAll("[data-go]")).forEach(function (t) {
        t.addEventListener("click", function () {
            var n = parseInt(t.getAttribute("data-go"), 10);
            if (mode === "pin") {
                var y = window.scrollY + hero.getBoundingClientRect().top - hdr() + STORY_LEN * ((n - 1) / STEPS + 0.02);
                window.scrollTo({ top: y, behavior: "smooth" });
            } else {
                stopAuto(); autoDone = true;
                setStep(n);
                fills.forEach(function (f, j) { f.style.transition = "none"; f.style.width = j < n ? "100%" : "0%"; });
            }
        });
    });

    window.addEventListener("scroll", onScroll, { passive: true });
    /* No celular (iPhone principalmente) a barra do navegador some/aparece durante
       a rolagem e dispara "resize" só de altura. Refazer o layout nesse caso
       parava a sequência na etapa 1 ("Dados"). Só refaz quando a largura muda,
       ou no modo fixo do desktop, que depende da altura da janela. */
    var rt, lastW = window.innerWidth;
    window.addEventListener("resize", function () {
        clearTimeout(rt);
        rt = setTimeout(function () {
            var w = window.innerWidth;
            if (w === lastW && mode !== "pin") return;
            lastW = w;
            layout();
        }, 150);
    });
    layout();
})();
