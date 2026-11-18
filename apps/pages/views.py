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


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

# NOVIDADES das ferramentas (SIGE, automações, modelos, Jarvis).
# A seção "Novidades" da home só aparece quando esta lista tem itens.
# Coloque as mais recentes primeiro. Exemplo:
#     {"data": "11/2026", "ferramenta": "SIGE", "texto": "Novo módulo de fluxo de caixa projetado."},
NOVIDADES = []

# Painel ilustrativo do topo da home (valores fictícios, marcados como "dados ilustrativos").
DRE_ILUSTRATIVA = [
    ("Receita bruta", "1.248.300", "", True),
    ("(−) Deduções", "−149.796", "", False),
    ("Receita líquida", "1.098.504", "", True),
    ("(−) Custos variáveis", "−512.430", "", False),
    ("Margem de contribuição", "586.074", "53,4%", True),
    ("(−) Despesas fixas", "−401.220", "", False),
    ("Resultado operacional", "184.854", "16,8%", True),
]
CAIXA_SEMANAS = [182, 196, 171, 188, 160, 138, 92, 121, 149, 174, 201, 226]  # R$ mil
CAIXA_MINIMO = 110
FOTO_SOBRE = "img/sobre/leles.webp"


def home(request):
    from django.contrib.staticfiles import finders

    escala_max, altura = 230, 120
    barras = [
        {"altura": round(v / escala_max * altura), "alerta": v < CAIXA_MINIMO}
        for v in CAIXA_SEMANAS
    ]
    contexto = {
        "dre": [
            {"rotulo": r, "valor": val, "pct": pct, "total": tot}
            for r, val, pct, tot in DRE_ILUSTRATIVA
        ],
        "barras": barras,
        "linha_minimo": round(CAIXA_MINIMO / escala_max * altura),
        "novidades": NOVIDADES,
        "foto_sobre": FOTO_SOBRE if finders.find(FOTO_SOBRE) else None,
    }
    return render(request, "pages/home.html", contexto)


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
