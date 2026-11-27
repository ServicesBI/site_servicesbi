from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse

# Páginas públicas: usadas no sitemap.xml e no export estático.
PAGINAS_PUBLICAS = [
    ("/", "1.0"),
    ("/consultoria-financeira/", "0.9"),
    ("/power-bi/", "0.8"),
    ("/produtos/", "0.8"),
    ("/cases/", "0.7"),
    ("/automacoes/", "0.8"),
    ("/sobre/", "0.7"),
    ("/contato/", "0.7"),
    ("/python/", "0.6"),
    ("/excel/", "0.6"),
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

# Faixa corrida (marquee) logo abaixo do hero: pastas com os produtos.
# (título, linha pequena, etiqueta do "arquivo" no hover, url name, imagem claro, imagem escuro, selo)
SIGE_DEMO_URL = "https://servicesbi.com.br/sige-demo/login/"
# Painel de metas da home (vendedores fictícios). Valores em R$ mil por mês: setembro, outubro, novembro.
METAS_MESES = ["Setembro", "Outubro", "Novembro"]
METAS_VENDEDORES = [
    # (nome, cidade, foto, faturamento por mês, meta por mês)
    ("Caroline Mendes", "Porto Alegre · RS", "caroline", [2610, 2770, 3080], [2700, 2750, 2840]),
    ("Rafael Souza", "Curitiba · PR", "rafael", [2480, 2350, 2540], [2400, 2500, 2600]),
    ("Juliana Alves", "Florianópolis · SC", "juliana", [2010, 2290, 2420], [2300, 2300, 2400]),
    ("Marcos Lima", "São Paulo · SP", "marcos", [2350, 2120, 1840], [2300, 2350, 2450]),
    ("Mariana Sato", "Belo Horizonte · MG", "mariana", [1980, 2150, 2330], [2100, 2200, 2250]),
]


def _metas_dados():
    return {
        "meses": METAS_MESES,
        "vendedores": [
            {"nome": n, "cidade": c, "foto": static(f"img/home/vendedores/{f}.webp"), "fat": fat, "meta": meta}
            for n, c, f, fat, meta in METAS_VENDEDORES
        ],
    }


# Cards da seção "Ferramentas" da home
FERRAMENTAS_HOME = [
    # (título, tipo, selo, o que faz, para quem, texto do link, url (nome da rota ou "wa_jarvis"), imagem clara, imagem escura)
    ("SIGE", "ERP · Gestão integrada", "Demo disponível",
     "Cadastros, compras, vendas, financeiro, estoque e fluxo de caixa no mesmo sistema.",
     "Empresas que controlam a operação em planilhas e sistemas que não conversam entre si.",
     "Conhecer o SIGE", "pages:sige_produto", "img/home/portfolio/destaques/sige-servicesbi.webp", None),
    ("Jarvis", "Assistente de IA", "Em desenvolvimento",
     "Assistente operacional para financeiro, documentos, e-mail e agenda.",
     "Empresas que querem acesso antecipado como primeiros clientes.",
     "Entrar na lista de espera", "wa_jarvis", "img/home/Services_Jarvis/orquestrador.webp", None),
    ("Automações n8n", "Python · n8n", "Sob medida",
     "Relatórios enviados sozinhos por e-mail e WhatsApp, conciliação de planilhas e integração entre sistemas.",
     "Equipes que perdem horas toda semana copiando e colando dados.",
     "Ver automações", "pages:automacoes", "img/automacoes/hero/hero_automacoes_light.webp", "img/automacoes/hero/hero_automacoes_dark.webp"),
    ("Excel corporativo", "Modelos financeiros", "Templates prontos",
     "Fluxo de caixa, DRE e precificação com Power Query e VBA, prontos para usar no dia seguinte.",
     "Quem precisa de controle financeiro agora, sem implantar um sistema.",
     "Ver modelos", "pages:excel", "img/home/pastas/excel_dashboard.webp", None),
]


ANCORAS_PRODUTOS = {"SIGE": "sige", "Jarvis": "jarvis", "Automações n8n": "automacoes", "Excel corporativo": "excel"}

# Detalhe de cada produto na página Nossos Produtos
PRODUTOS_DETALHE = [
    {
        "ancora": "sige", "tipo": "ERP · Gestão integrada", "selo": "Demo disponível",
        "titulo": "SIGE", "chamada": "a operação inteira <em>num sistema só.</em>",
        "texto": "ERP da ServicesBI que reúne cadastros, compras, vendas, estoque e financeiro. O fluxo de caixa sai direto das operações do dia a dia, sem planilha paralela.",
        "itens": ["Cadastros de clientes, fornecedores e produtos", "Compras e vendas ligadas ao estoque", "Contas a pagar, a receber e fluxo de caixa", "Dados prontos para os painéis em Power BI"],
        "para": "Empresas que controlam a operação em planilhas e sistemas que não conversam entre si.",
        "cta": "Conhecer o SIGE", "destino": "sige",
        "img": "img/home/portfolio/destaques/sige-servicesbi.webp", "img_dark": None,
    },
    {
        "ancora": "jarvis", "tipo": "Assistente de IA", "selo": "Em desenvolvimento",
        "titulo": "Jarvis", "chamada": "um assistente para <em>a rotina do escritório.</em>",
        "texto": "Assistente operacional com IA para o financeiro, os documentos, o e-mail e a agenda. Está em desenvolvimento e abre primeiro para uma lista de empresas parceiras.",
        "itens": ["Apoio às rotinas do financeiro", "Leitura e organização de documentos", "Triagem de e-mails", "Agenda e lembretes"],
        "para": "Empresas que querem acesso antecipado como primeiros clientes.",
        "cta": "Entrar na lista de espera", "destino": "jarvis",
        "img": "img/home/Services_Jarvis/orquestrador.webp", "img_dark": None,
    },
    {
        "ancora": "automacoes", "tipo": "Python · n8n", "selo": "Sob medida",
        "titulo": "Automações n8n", "chamada": "o trabalho repetitivo <em>roda sozinho.</em>",
        "texto": "Robôs em Python e fluxos no n8n que assumem as tarefas que hoje consomem horas da equipe, com o resultado chegando pronto no e-mail ou no WhatsApp.",
        "itens": ["Relatórios enviados sozinhos por e-mail e WhatsApp", "Conciliação de planilhas e extratos", "Integração entre sistemas, planilhas e APIs", "Alertas quando um indicador sai do esperado"],
        "para": "Equipes que perdem horas toda semana copiando e colando dados.",
        "cta": "Quero automatizar uma rotina", "destino": "wa",
        "img": "img/automacoes/hero/hero_automacoes_light.webp", "img_dark": "img/automacoes/hero/hero_automacoes_dark.webp",
    },
    {
        "ancora": "excel", "tipo": "Modelos financeiros", "selo": "Templates prontos",
        "titulo": "Excel corporativo", "chamada": "controle financeiro <em>no dia seguinte.</em>",
        "texto": "Modelos de fluxo de caixa, DRE e precificação feitos com Power Query e VBA, prontos para usar sem implantar um sistema.",
        "itens": ["Fluxo de caixa projetado", "DRE gerencial", "Precificação e margem por produto", "Atualização com Power Query e rotinas em VBA"],
        "para": "Quem precisa de controle financeiro agora, sem implantar um sistema.",
        "cta": "Quero um modelo", "destino": "wa",
        "img": "img/home/pastas/excel_dashboard.webp", "img_dark": None,
    },
]

HERO_CARDS_PRODUTOS = [
    ("SIGE · ERP", "#sige", "img/home/portfolio/destaques/sige-servicesbi.webp", "img/home/portfolio/destaques/sige-servicesbi.webp"),
    ("Automações n8n", "#automacoes", "img/automacoes/hero/hero_automacoes_light.webp", "img/automacoes/hero/hero_automacoes_dark.webp"),
    ("Excel corporativo", "#excel", "img/home/pastas/excel_dashboard.webp", "img/home/pastas/excel_dashboard.webp"),
]


def _ferramentas_home():
    itens = []
    for titulo, tipo, selo, faz, para, link, rota, img, img_dark in FERRAMENTAS_HOME:
        externo = rota == "wa_jarvis"
        itens.append({
            "titulo": titulo, "tipo": tipo, "selo": selo, "faz": faz, "para": para, "link": link,
            "url": "" if externo else reverse(rota), "externo": externo,
            "img": img, "img_dark": img_dark or img,
            "ancora": ANCORAS_PRODUTOS.get(titulo, ""),
        })
    return itens


# Cases da home (clientes anônimos)
CASES_HOME = [
    # (setor, título, selo da imagem, imagem, desafio, o que foi feito, resultado)
    ("Educação · Financeiro", "Gestão financeira de uma instituição de ensino", "Dados ilustrativos",
     "img/home/portfolio/destaques/dashboard-financeiro.webp",
     "Receitas, inadimplência e contas a pagar e a receber em planilhas separadas, sem visão consolidada.",
     "Painéis de receitas, inadimplência, fluxo de caixa e DRE, com projeções financeiras.",
     "Diretoria passou a decidir com base em indicadores consolidados."),
    ("Saúde · Compras e suprimentos", "Indicadores de compras de um hospital", "Dados ilustrativos",
     "img/home/portfolio/destaques/dashboard-compras.webp",
     "Compras, contratos e fornecedores sem acompanhamento de saving, prazos e desempenho.",
     "Controles e relatórios de compras, estoques, saving e desempenho de fornecedores.",
     "Negociações apoiadas em histórico e indicadores, e não em impressões."),
    ("Instituição nacional · Dados e automação", "Consolidação de dados financeiros e automação", "Exemplo de fluxo",
     "img/home/portfolio/destaques/robos-python-operacional.webp",
     "Dados financeiros e acadêmicos espalhados e demandas manuais repetitivas.",
     "Integração das bases, análises de inadimplência, receitas e orçamento, e rotinas automatizadas.",
     "Rotinas manuais transformadas em relatórios automáticos."),
]


# Cards de imagem do hero: (título, destino: "wa" ou nome da rota ou âncora "#...", imagem clara, imagem escura)
HERO_CARDS_PADRAO = [
    ("Diagnóstico inicial", "wa", "img/home/cards/light/card04.webp", "img/home/cards/dark/card04.webp"),
    ("Análise de dados", "pages:powerbi", "img/home/cards/light/card02.webp", "img/home/cards/dark/card02.webp"),
    ("Automações", "pages:automacoes", "img/home/cards/light/card03.webp", "img/home/cards/dark/card03.webp"),
]
HERO_CARDS_POWERBI = [
    ("Conexão com banco de dados", "#entrega-title", "img/home/cards/light/card03.webp", "img/home/cards/dark/card03.webp"),
    ("ETL", "#entrega-title", "img/home/cards/light/card01.webp", "img/home/cards/dark/card01.webp"),
    ("Modelagem", "#entrega-title", "img/home/cards/light/card02.webp", "img/home/cards/dark/card02.webp"),
]


def _hero_cards(cards):
    return [
        {"titulo": t, "wa": d == "wa", "url": d if d.startswith("#") or d == "wa" else reverse(d), "claro": c, "escuro": e}
        for t, d, c, e in cards
    ]


# Pastas da página de BI: cada pasta é um dashboard (clique abre a imagem grande)
PASTAS_POWERBI = [
    # (título, subtítulo, selo, imagem clara, imagem escura, link público do Power BI ou None)
    ("Desempenho comercial", "Faturamento, margem e vendedores", "Interativo", "img/powerbi/dashboards/desempenho-comercial.webp", None,
     "https://app.powerbi.com/view?r=eyJrIjoiMjI2NWNjNjUtZWM1NS00ZDc3LTgzODAtYWM4M2Q4ZTI5YmQ2IiwidCI6ImQxZTQzMTViLTY1NTktNGQwOC1hNDRlLTI1MDgwYzMyYTA2ZiJ9"),
    ("DRE gerencial", "Realizado vs. previsto e análise vertical", "Interativo", "img/powerbi/dashboards/dre-real-vs-meta.webp", None,
     "https://app.powerbi.com/view?r=eyJrIjoiM2JjODRiZmUtMzRjMC00NDQyLTkxYzktNmI5ZDY3YjhiMDdiIiwidCI6ImQxZTQzMTViLTY1NTktNGQwOC1hNDRlLTI1MDgwYzMyYTA2ZiJ9"),
    ("Realizado vs. Meta", "Faturamento, metas e vendedores", "Interativo", "img/powerbi/dashboards/realizado-vs-meta.webp", None,
     "https://app.powerbi.com/view?r=eyJrIjoiODkwZmQwOWYtNWYyMy00NjZiLWI2MDYtMWExMDU5MWE5ZWU1IiwidCI6ImQxZTQzMTViLTY1NTktNGQwOC1hNDRlLTI1MDgwYzMyYTA2ZiJ9"),
    ("Real x Meta completo", "Tempo, time, produtos e recomendações", "Interativo", "img/powerbi/dashboards/real-x-meta-completo.webp", None,
     "https://app.powerbi.com/view?r=eyJrIjoiY2I5NzA2YzQtYTRjNS00ZWQwLTg4MmItY2I0MTdjZTFkMmM4IiwidCI6ImQxZTQzMTViLTY1NTktNGQwOC1hNDRlLTI1MDgwYzMyYTA2ZiJ9"),
    ("Dashboard financeiro", "Contas a pagar e a receber", "Interativo", "img/home/portfolio/destaques/dashboard-financeiro.webp", None,
     "https://app.powerbi.com/view?r=eyJrIjoiYzE4NDU2Y2MtN2RlOS00MGQzLWEwODItNWI5Nzk0NzY2NDk2IiwidCI6ImQxZTQzMTViLTY1NTktNGQwOC1hNDRlLTI1MDgwYzMyYTA2ZiJ9"),
    ("Performance de vendas", "Vendedores e produtos", "Interativo", "img/home/portfolio/destaques/dashboard-compras.webp", None,
     "https://app.powerbi.com/view?r=eyJrIjoiZWNhYTBjNjctNGUzOS00ZDdjLTg2NWEtYzU5MmUxZTI0NDJmIiwidCI6ImQxZTQzMTViLTY1NTktNGQwOC1hNDRlLTI1MDgwYzMyYTA2ZiJ9"),
]


def _pastas_dashboards():
    return [
        {"titulo": t, "sub": sub, "etiqueta": "", "demo": False, "zoom": True, "url": link or static(c),
         "claro": c, "escuro": e or c, "selo": selo, "embed": link}
        for t, sub, selo, c, e, link in PASTAS_POWERBI
    ]


# Autodiagnóstico da home: (sintoma, descrição, como a ServicesBI resolve)
DORES_DIAGNOSTICO = [
    # (sintoma, descrição, solução curta, o que a ServicesBI faz, resultado)
    ("Não sei quanto vai sobrar no caixa", "Você não sabe ao certo quanto vai sobrar ou faltar nos próximos 30, 60 ou 90 dias.", "Caixa projetado para 12 semanas",
     "Montamos o fluxo de caixa projetado de 12 semanas com as contas reais a pagar e a receber.", "Você enxerga um aperto com semanas de antecedência e decide antes dele chegar."),
    ("Decido no \u201cachismo\u201d", "Sem DRE gerencial, não dá para saber quais produtos ou serviços dão lucro e quais dão prejuízo.", "DRE gerencial e margem por produto",
     "Estruturamos a DRE gerencial e a margem de contribuição por produto e serviço.", "Você sabe o que dá lucro, o que dá prejuízo e onde cortar ou investir."),
    ("Vivo de planilha manual", "Vendas, estoque e financeiro em arquivos que não batem e geram retrabalho todo mês.", "Dados integrados e rotinas automatizadas",
     "Integramos vendas, estoque e financeiro e automatizamos a atualização dos números.", "Os números batem sozinhos e o fechamento deixa de levar dias."),
    ("Cada área faz do seu jeito", "Compras, comercial e estoque operam separados e acabam drenando o caixa.", "Indicadores únicos para todas as áreas",
     "Definimos indicadores únicos e um painel compartilhado entre compras, comercial e estoque.", "Todas as áreas olham o mesmo número e o caixa para de vazar."),
]

MARQUEE_PASTAS = [
    # Linha 1
    ("SIGE ServicesBI", "ERP completo com demo", "ERP · demo aberta", "demo",
     "img/home/portfolio/destaques/sige-servicesbi.webp", None, ""),
    ("Jarvis", "Assistente operacional", "IA · em desenvolvimento", "pages:jarvis",
     "img/home/Services_Jarvis/orquestrador.webp", None, "em desenvolvimento"),
    ("Power BI", "Painéis sob medida", "Dashboards · BI", "pages:powerbi",
     "img/powerbi/hero/hero_powerbi_light.webp", "img/powerbi/hero/hero_powerbi_dark.webp", ""),
    # Linha 2
    ("Automações n8n", "Rotinas sem retrabalho", "n8n · fluxo", "pages:automacoes",
     "img/automacoes/hero/hero_automacoes_light.webp", "img/automacoes/hero/hero_automacoes_dark.webp", ""),
    ("Projetos em Python", "Sistemas internos", ".py · sistema web", "pages:python",
     "img/python/hero/hero_python_light.webp", "img/python/hero/hero_python_dark.webp", ""),
    ("Modelos em Excel", "Planilhas prontas", "", "pages:excel",
     "img/home/pastas/excel_dashboard.webp", "img/home/pastas/excel_dashboard.webp", ""),
]


# Etapa "Decisão" do hero: saídas para o caixa abaixo do mínimo (exemplo ilustrativo).
# efeito = ganho no saldo de caixa por semana (R$ mil); custo em R$ mil.
SEMANA_ATUAL = 3
OPCOES_DECISAO = [
    {"id": "estoque", "titulo": "Adiar a compra de estoque em 2 semanas",
     "detalhe": "+R$ 35 mil nas sem. 6 e 7 · custo R$ 0",
     "efeito": {6: 35, 7: 35}, "custo": 0, "recomendado": True},
    {"id": "fornecedor", "titulo": "Renegociar prazo do fornecedor principal",
     "detalhe": "+R$ 25 mil nas sem. 7 e 8 · custo R$ 0",
     "efeito": {7: 25, 8: 25}, "custo": 0, "recomendado": False},
    {"id": "recebiveis", "titulo": "Antecipar recebíveis de cartão",
     "detalhe": "+R$ 40 mil nas sem. 5 a 8 · taxa R$ 1,2 mil",
     "efeito": {5: 40, 6: 40, 7: 40, 8: 40, 9: 20, 10: -1.2, 11: -1.2, 12: -1.2}, "custo": 1.2, "recomendado": False},
]


def _num(texto):
    """'1.248.300' / '−149.796' -> int."""
    return int(texto.replace(".", "").replace("−", "-"))


def _br(valor, casas=1):
    """Número no formato brasileiro: 1234.5 -> '1.234,5'."""
    s = f"{valor:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _indicadores_hero():
    """Indicadores e cascata da etapa 'Indicadores' do hero, calculados da DRE ilustrativa."""
    v = {rotulo: _num(valor) for rotulo, valor, _pct, _tot in DRE_ILUSTRATIVA}
    rl = v["Receita líquida"]
    cv = -v["(−) Custos variáveis"]
    mc = v["Margem de contribuição"]
    df = -v["(−) Despesas fixas"]
    res = v["Resultado operacional"]
    mc_pct = mc / rl * 100
    res_pct = res / rl * 100
    pe = df / (mc / rl)
    folga = (rl - pe) / rl * 100
    indicadores = {
        "mc_pct": _br(mc_pct) + "%",
        "mc_raw": f"{mc_pct:.1f}",
        "mc_dash": f"{mc_pct / 100 * 94.25:.2f}",
        "res_pct": _br(res_pct) + "%",
        "res_raw": f"{res_pct:.1f}",
        "res_mil": _br(res / 1000),
        "pe_mil": _br(pe / 1000, 0),
        "folga": _br(folga),
        "sobra": _br(res_pct, 2),
    }
    passos = [  # (base, topo, tipo, rótulo, valor exibido) em R$ mil
        (0, rl, "pos", "Receita líquida", rl),
        (mc, rl, "neg", "Custos variáveis", -cv),
        (0, mc, "pos", "Margem", mc),
        (res, mc, "neg", "Despesas fixas", -df),
        (0, res, "res", "Resultado", res),
    ]
    cascata = []
    for i, (base, topo, tipo, rotulo, valor) in enumerate(passos):
        texto = _br(abs(valor) / 1000, 0)
        cascata.append({
            "i": i,
            "tipo": tipo,
            "rotulo": rotulo,
            "texto": ("−" + texto) if valor < 0 else texto,
            "base": f"{base / rl * 100:.2f}",
            "altura": f"{(topo - base) / rl * 100:.2f}",
            "topo": f"{topo / rl * 100:.2f}",
        })
    return indicadores, cascata


def _contexto_modelo():
    """Contexto do modelo de página (base: Consultoria Financeira), usado por todas as páginas."""
    from django.contrib.staticfiles import finders

    escala_max = 240
    barras = [
        {"pct": f"{v / escala_max * 100:.2f}", "alerta": v < CAIXA_MINIMO, "semana": i + 1}
        for i, v in enumerate(CAIXA_SEMANAS)
    ]
    # Primeira semana abaixo do mínimo: alimenta o alerta da etapa "Decisão" do hero.
    alerta = None
    for i, v in enumerate(CAIXA_SEMANAS):
        if v < CAIXA_MINIMO:
            alerta = {
                "semana": i + 1,
                "falta": CAIXA_MINIMO - v,
                "pos": f"{(i + 0.5) / len(CAIXA_SEMANAS) * 100:.2f}",
                "base": barras[i]["pct"],
            }
            break
    indicadores, cascata = _indicadores_hero()
    decisao = {
        "semanas": CAIXA_SEMANAS,
        "minimo": CAIXA_MINIMO,
        "escala": escala_max,
        "opcoes": [
            {"id": o["id"], "efeito": {str(k): v for k, v in o["efeito"].items()}, "custo": o["custo"]}
            for o in OPCOES_DECISAO
        ],
    }
    if alerta:
        alerta["prazo"] = alerta["semana"] - SEMANA_ATUAL
        alerta["valor"] = CAIXA_SEMANAS[alerta["semana"] - 1]
    contexto = {
        "dre": [
            {"rotulo": r, "valor": val, "pct": pct, "total": tot}
            for r, val, pct, tot in DRE_ILUSTRATIVA
        ],
        "barras": barras,
        "linha_minimo": f"{CAIXA_MINIMO / escala_max * 100:.2f}",
        "caixa_minimo": CAIXA_MINIMO,
        "alerta": alerta,
        "indicadores": indicadores,
        "cascata": cascata,
        "opcoes_decisao": OPCOES_DECISAO,
        "decisao": decisao,
        "sige_demo_url": SIGE_DEMO_URL,
        "hero_cards": _hero_cards(HERO_CARDS_PADRAO),
        "dores": DORES_DIAGNOSTICO,
        "metas": _metas_dados(),
        "ferramentas": _ferramentas_home(),
        "cases": CASES_HOME,
        "marquee_pastas": [
            {"titulo": t, "sub": sub, "etiqueta": et, "demo": u == "demo",
             "url": SIGE_DEMO_URL if u == "demo" else reverse(u),
             "claro": c, "escuro": e or c, "selo": selo}
            for t, sub, et, u, c, e, selo in MARQUEE_PASTAS
        ],
        "novidades": NOVIDADES,
        "foto_sobre": FOTO_SOBRE if finders.find(FOTO_SOBRE) else None,
    }
    return contexto


def home(request):
    return render(request, "pages/home.html", _contexto_modelo())


def _redirecionar(request, destino, titulo):
    """Página que só encaminha o visitante para outro endereço.
    O site publicado é estático (cloudflare_dist), então o redirecionamento é feito
    no próprio HTML (meta refresh), sem depender do Nginx."""
    return render(request, "pages/redirecionar.html", {"destino": destino, "titulo": titulo})


def sige_produto_page(request):
    # /produtos/sige/ — endereço oficial do SIGE no site.
    # Por enquanto leva à página do SIGE (apresentação, módulos, planos e login da demo).
    return _redirecionar(request, SIGE_DEMO_URL, "SIGE | ServicesBI")


def sige_institucional_page(request):
    # Endereço antigo: agora aponta para /produtos/sige/ (antes era uma cópia da Home).
    return _redirecionar(request, "/produtos/sige/", "SIGE | ServicesBI")


def jarvis_page(request):
    return render(request, "pages/jarvis.html", _contexto_modelo())


def python_page(request):
    return render(request, "pages/python.html", _contexto_modelo())


def _contexto_bi():
    # Contexto da página BI & Dashboards, usado também como base de Nossos Produtos, Cases e Sobre.
    contexto = _contexto_modelo()
    contexto["hero_cards"] = _hero_cards(HERO_CARDS_POWERBI)
    contexto["marquee_pastas"] = _pastas_dashboards()
    return contexto


def powerbi_page(request):
    return render(request, "pages/powerbi.html", _contexto_bi())


def produtos_page(request):
    contexto = _contexto_modelo()
    contexto["hero_cards"] = _hero_cards(HERO_CARDS_PRODUTOS)
    contexto["produtos"] = [dict(p, img_dark=p["img_dark"] or p["img"]) for p in PRODUTOS_DETALHE]
    contexto["ancoras"] = True
    return render(request, "pages/produtos.html", contexto)


def cases_page(request):
    return render(request, "pages/cases.html", _contexto_bi())


def automacoes_page(request):
    return render(request, "pages/automacoes.html", _contexto_modelo())


def excel_page(request):
    return render(request, "pages/excel.html", _contexto_modelo())


def curriculo_page(request):
    return render(request, "pages/curriculo.html", _contexto_modelo())


def contato_page(request):
    return render(request, "pages/contato.html", _contexto_modelo())


def consultoria_page(request):
    # A consultoria financeira é a própria home: o endereço antigo mostra a mesma página
    # (com canonical apontando para "/" para não duplicar no Google).
    return home(request)


def sobre_page(request):
    return render(request, "pages/sobre.html", _contexto_bi())


def robots_txt(request):
    return render(request, "robots.txt", content_type="text/plain; charset=utf-8")


def sitemap_xml(request):
    return render(
        request,
        "sitemap.xml",
        {"paginas": PAGINAS_PUBLICAS},
        content_type="application/xml; charset=utf-8",
    )
