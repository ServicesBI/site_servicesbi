from urllib.parse import quote

from django.conf import settings

WHATSAPP_NUMERO = "5561993029988"


def _wa(mensagem):
    return f"https://wa.me/{WHATSAPP_NUMERO}?text={quote(mensagem, safe='')}"


def site(request):
    """Variáveis globais usadas em todas as páginas."""
    return {
        "SITE_URL": getattr(settings, "SITE_URL", "https://www.servicesbi.com.br"),
        "CLARITY_ID": getattr(settings, "CLARITY_ID", ""),
        "WHATSAPP_NUMERO": WHATSAPP_NUMERO,
        "WA_GERAL": _wa("Olá Leles, vi o site da ServicesBI e gostaria de saber mais sobre a consultoria financeira."),
        "WA_DIAGNOSTICO": _wa("Olá Leles, vi o site da ServicesBI e gostaria de agendar o diagnóstico financeiro gratuito."),
        "EMAIL_CONTATO": "servicesbi.ltda@gmail.com",
        "LINKEDIN_URL": "https://www.linkedin.com/in/jrleles/",
    }
