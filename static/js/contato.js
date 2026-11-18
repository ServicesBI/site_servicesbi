(function () {
    // Formulário de contato: monta a mensagem com os dados preenchidos e abre o WhatsApp.
    // Não depende de servidor/webhook. Para trocar por n8n ou Formspree no futuro,
    // basta substituir a função abrirWhatsApp por um fetch() ao endpoint escolhido.
    var WHATSAPP_NUMERO = "5561993029988";

    var form = document.getElementById("contato-form");
    if (!form) return;

    var submitBtn = document.getElementById("contato-submit");
    var erroEl = document.getElementById("contato-form-erro");
    var sucessoEl = document.getElementById("contato-estado-sucesso");
    var fallbackLink = document.getElementById("contato-wa-fallback");

    function valor(nome) {
        var el = form.querySelector('[name="' + nome + '"]');
        return el ? el.value.trim() : "";
    }

    function montarMensagem(d) {
        var linhas = [
            "Olá Leles, vim pelo site da ServicesBI e gostaria de solicitar um contato.",
            "",
            "*Nome:* " + d.nome,
            "*WhatsApp:* " + d.whatsapp
        ];
        if (d.empresa) linhas.push("*Empresa:* " + d.empresa);
        linhas.push("*Maior desafio:* " + d.desafio);
        if (d.mensagem) {
            linhas.push("");
            linhas.push(d.mensagem);
        }
        return linhas.join("\n");
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        erroEl.hidden = true;

        // Honeypot anti-spam: se um robô preencheu, não faz nada.
        if (valor("website")) return;

        var dados = {
            nome: valor("nome"),
            whatsapp: valor("whatsapp"),
            empresa: valor("empresa"),
            desafio: valor("tipo_demanda"),
            mensagem: valor("mensagem")
        };

        var digitos = dados.whatsapp.replace(/\D/g, "");
        if (!dados.nome || digitos.length < 10 || !dados.desafio) {
            erroEl.hidden = false;
            erroEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
            return;
        }

        var url = "https://wa.me/" + WHATSAPP_NUMERO + "?text=" + encodeURIComponent(montarMensagem(dados));

        if (fallbackLink) fallbackLink.href = url;
        var janela = window.open(url, "_blank", "noopener");
        if (!janela) window.location.href = url; // pop-up bloqueado: abre na mesma aba

        form.hidden = true;
        sucessoEl.hidden = false;
        sucessoEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
        submitBtn.blur();
    });
})();
