(function () {
    // Quando o workflow do n8n estiver em produção, inserir aqui a Production URL do webhook.
    // Exemplo: https://SEU_DOMINIO_N8N/webhook/servicesbi-contato
    const N8N_WEBHOOK_URL = "";

    var form = document.getElementById("contato-form");
    var submitBtn = document.getElementById("contato-submit");
    var estadoPendente = document.getElementById("contato-estado-pendente");
    var estadoSucesso = document.getElementById("contato-estado-sucesso");
    var estadoErro = document.getElementById("contato-estado-erro");

    if (!form) return;

    function ocultarEstados() {
        estadoPendente.hidden = true;
        estadoSucesso.hidden = true;
        estadoErro.hidden = true;
    }

    function mostrarEstado(el) {
        ocultarEstados();
        el.hidden = false;
        el.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    function setEnviando(enviando) {
        submitBtn.disabled = enviando;
        submitBtn.textContent = enviando ? "Enviando..." : "Enviar mensagem";
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        ocultarEstados();

        // Honeypot anti-spam — bot preencheu, silêncio
        var honeypot = form.querySelector('[name="website"]');
        if (honeypot && honeypot.value) {
            mostrarEstado(estadoSucesso);
            return;
        }

        // Integração ainda não configurada
        if (!N8N_WEBHOOK_URL) {
            form.hidden = true;
            mostrarEstado(estadoPendente);
            return;
        }

        var data = {
            nome: form.querySelector('[name="nome"]').value.trim(),
            email: form.querySelector('[name="email"]').value.trim(),
            whatsapp: form.querySelector('[name="whatsapp"]').value.trim(),
            tipo_demanda: form.querySelector('[name="tipo_demanda"]').value,
            mensagem: form.querySelector('[name="mensagem"]').value.trim(),
            origem: "site-servicesbi-contato",
            pagina: window.location.href,
            user_agent: navigator.userAgent,
            enviado_em: new Date().toISOString()
        };

        setEnviando(true);

        fetch(N8N_WEBHOOK_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        })
            .then(function (response) {
                if (response.ok) {
                    form.hidden = true;
                    mostrarEstado(estadoSucesso);
                } else {
                    mostrarEstado(estadoErro);
                }
            })
            .catch(function () {
                mostrarEstado(estadoErro);
            })
            .finally(function () {
                setEnviando(false);
            });
    });
})();
