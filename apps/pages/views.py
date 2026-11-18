from django.shortcuts import render

# Páginas públicas: usadas no sitemap.xml e no export estático.
PAGINAS_PUBLICAS = [
    ("/", "1.0"),
    ("/consultoria-financeira/", "0.9"),
    ("/power-bi/", "0.8"),
    ("/automacoes/", "0.8"),
    ("/sobre/", "0.7"),
    ("/contato/", "0.7"),
    ("/python/", "0.6"),
    ("/excel/", "0.6"),
    ("/sige-servicesbi/", "0.5"),
    ("/jarvis/", "0.4"),
    ("/curriculo/", "0.4"),
]


def home(request):
    return render(request, "pages/home.html")


def sige_institucional_page(request):
    return render(request, "pages/sige_institucional.html")


def jarvis_page(request):
    return render(request, "pages/jarvis.html")


def python_page(request):
    return render(request, "pages/python.html")


def powerbi_page(request):
    return render(request, "pages/powerbi.html")


def automacoes_page(request):
    return render(request, "pages/automacoes.html")


def excel_page(request):
    return render(request, "pages/excel.html")


def curriculo_page(request):
    return render(request, "pages/curriculo.html")


def contato_page(request):
    return render(request, "pages/contato.html")


def consultoria_page(request):
    return render(request, "pages/consultoria_financeira.html")


def sobre_page(request):
    return render(request, "pages/sobre.html")


def robots_txt(request):
    return render(request, "robots.txt", content_type="text/plain; charset=utf-8")


def sitemap_xml(request):
    return render(
        request,
        "sitemap.xml",
        {"paginas": PAGINAS_PUBLICAS},
        content_type="application/xml; charset=utf-8",
    )
