# ServicesBI — Guia de Identidade Visual (v2026)

> **Fonte de verdade da marca ServicesBI.** Versão técnica do *Manual de Identidade Visual* (PDF).
> Vale para o site, propostas, relatórios, apresentações e dashboards em Power BI.
> Substitui `SERVICESBI_COLOR_PALETTE.md` (paleta antiga com accent `#CA3A18`).
> **Última atualização: 23/11/2026** — tema escuro passou a usar a paleta do SIGE (seção 4) e foram registradas as decisões de design das conversas (seção 13).
> A parte técnica (código, rotas, publicação) está em `docs/SERVICESBI_PROGRAMACAO.md`.

---

## 1. Essência da marca

**Quem somos:** consultoria financeira que usa análise de dados, Business Intelligence e automação para organizar, controlar e fazer crescer pequenas e médias empresas.

**O que a identidade precisa transmitir:** clareza · precisão · confiança · proximidade.

---

## 2. Logo

| Arquivo | Uso |
|---|---|
| `static/img/brand/logo-servicesbi.png` | Símbolo original (azul e verde), fundo transparente (410×410 px) |
| `static/img/brand/logo-servicesbi-claro.png` / `-claro-96.webp` | Versão do tema claro: disco petróleo com detalhes em laranja |
| `static/img/brand/logo-servicesbi-escuro.png` / `-escuro-96.webp` | Versão do tema escuro: disco preto-violeta com detalhes em violeta (**ainda não atualizada para o azul-aço do dark atual — pendente**) |
| `static/img/brand/favicon.ico` / `favicon-32.png` | Aba do navegador |
| `static/img/brand/apple-touch-icon.png` | Atalho no iPhone (fundo escuro) |
| `static/img/brand/icon-512.png` | Dados estruturados (Google), redes sociais |
| `static/img/brand/og-servicesbi.png` | Imagem de compartilhamento (WhatsApp, LinkedIn) 1200×630 |

**Assinatura em texto** (cabeçalho do site e documentos): `Services` na cor do título + `BI` na cor de destaque da marca (laranja `#E0812F` no claro, azul-aço `#7FB8CF` no escuro).

**Logo no cabeçalho e no rodapé** (`templates/includes/logo_mark.html`): as duas versões (claro e escuro) ficam no HTML e o CSS mostra a do tema ativo. Tamanho: **44 px no cabeçalho, 36 px no rodapé**.

**Favicon em tudo que abre no navegador:** site, SIGE, Jarvis, Compras e qualquer sistema novo da ServicesBI mostram o logo na aba. Três linhas logo depois do `<title>` (copiar os 3 arquivos para `static/img/brand/` do projeto):

```html
<link rel="icon" href="{% static 'img/brand/favicon.ico' %}" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{% static 'img/brand/favicon-32.png' %}">
<link rel="apple-touch-icon" href="{% static 'img/brand/apple-touch-icon.png' %}">
```

O favicon e a imagem de compartilhamento (`og-servicesbi.png`) ainda usam o logo original azul e verde.

```html
<a class="site-logo" href="/">Services<span>BI</span></a>
```

**Regras de uso**
- Área de proteção: espaço livre ao redor do símbolo igual a ¼ do seu diâmetro.
- Tamanho mínimo: 64 px (digital) e 20 mm (impresso). Abaixo disso o símbolo é só ícone (favicon, avatar).
- Fundos permitidos: bege, branco, petróleo e preto-azulado.
- Posição: canto superior esquerdo em capas, propostas e relatórios.

**Evite:** distorcer · mudar as cores · fundo sem contraste · girar ou adicionar sombra.

---

## 3. Cores — tema claro (padrão de documentos e tema light do site)

### 3.1 Cores da marca

| Nome | HEX | RGB | Uso |
|---|---|---|---|
| **Laranja ServicesBI** | `#E0812F` | 224 129 47 | Marca, áreas grandes, barras de gráfico, número principal da página |
| **Petróleo** | `#17545E` | 23 84 94 | Títulos, cabeçalhos de tabela, faixas de destaque, barras de gráfico |
| **Bege** | `#F3EFE7` | 243 239 231 | Fundo principal |
| **Grafite** | `#2B2B2B` | 43 43 43 | Texto corrido |
| **Vermelho** | `#C2553D` | 194 85 61 | Alertas e quedas (preenchimentos) |

### 3.2 Laranja de texto (acessibilidade)

| Nome | HEX | Uso |
|---|---|---|
| **Laranja de texto** | `#A9561A` | Links, rótulos, botões primários e qualquer texto laranja |

O `#E0812F` tem contraste de 2,5:1 sobre o bege e não serve para texto pequeno. O `#A9561A` tem 4,5:1 sobre bege e 5,2:1 sobre branco (padrão WCAG AA).

> **Regra:** laranja **preenchendo áreas** → `#E0812F` · laranja **em texto ou botão** → `#A9561A`.

### 3.3 Proporção em cada peça

Bege 55% · Petróleo 20% · Laranja 15% · Grafite e vermelho 10%. No máximo **um destaque laranja por página** em relatórios.

### 3.4 Tokens CSS (light) — `static/css/tokens.css`

```css
:root {
    --brand-laranja: #E0812F;
    --brand-petroleo: #17545E;
    --brand-bege: #F3EFE7;
    --brand-grafite: #2B2B2B;
    --brand-vermelho: #C2553D;

    --color-bg: var(--brand-bege);
    --color-bg-soft: #EBE5D9;          /* seções alternadas */
    --color-surface: #F8F5EF;
    --color-surface-strong: #FFFFFF;   /* cards */
    --color-text: var(--brand-petroleo);      /* títulos */
    --color-text-body: var(--brand-grafite);  /* texto */
    --color-text-muted: #6B6B6B;
    --color-border: #E1D9CB;
    --color-border-strong: #D2C8B6;
    --color-accent: #A9561A;           /* laranja de texto */
    --color-accent-bright: var(--brand-laranja);
    --color-on-accent: #FFFFFF;        /* texto sobre preenchimento de destaque */
    --color-button-bg: var(--color-accent);  /* botão primário */
    --color-button-text: #FFFFFF;
    --color-success: #2E7D4F;
    --color-warning: #B7791F;
    --color-danger: #A8432C;           /* vermelho para TEXTO */
    --color-info: #2F6690;
}
```

---

## 4. Cores — tema escuro (somente digital)

O site **abre no tema escuro** e o visitante pode alternar para o claro (botão ☀/☾). Documentos impressos e relatórios usam o tema claro.

> **Decisão de 22/11/2026:** o tema escuro do site usa **a mesma paleta do SIGE versão dark** (grafite-azulado, petróleo escuro e azul-aço). Substituiu o estilo "premium" preto + violeta + bege-dourado (inspirado na Xperiun), que vigorou de 18 a 22/11/2026. O tema claro não mudou. As cores foram tiradas do print do SIGE em produção, porque o código do SIGE fica em outro projeto (`D:\python\SIGE_ServicesBI`).

### 4.1 Cores

| Nome | HEX | Uso |
|---|---|---|
| **Grafite-azulado** | `#0A1217` | Fundo (também `theme-color` da barra do navegador no celular) |
| Superfície suave | `#0D171D` | Seções alternadas |
| Superfície | `#13222D` | Painéis e cards |
| Superfície forte | `#1F3340` | Cards em destaque |
| Borda forte | `#274151` | Bordas de destaque |
| Texto de título | `#E3EEF3` | Títulos |
| Texto corrido | `#9FB9C6` | Parágrafos |
| Texto secundário | `#6E8C9B` | Legendas, rótulos discretos |
| **Azul-aço** | `#7FB8CF` | Botões de ação, links, "BI" da assinatura, destaques em texto |
| **Aço claro** | `#A3D0E0` | Títulos em destaque |
| **Aço profundo** | `#4A8BA8` | Preenchimentos, barras de gráfico, números de passo |
| Âmbar | `#E5B567` | Alertas e metas (antes era o dourado) |
| Verde | `#30D08D` | Sucesso |
| Coral | `#FF6B7A` | Erros e quedas |

Botão de ação no escuro: fundo azul-aço `#7FB8CF` com texto `#0A1217`. Brilhos de fundo em azul-aço, com intensidade baixa (discretos como no SIGE).

**Correspondência entre os temas:** fundo bege → grafite-azulado · títulos petróleo → `#E3EEF3` · texto grafite → `#9FB9C6` · destaque laranja → azul-aço · botão laranja → botão azul-aço.

### 4.2 Tokens CSS (dark) — `static/css/tokens.css`

```css
html.theme-dark, body.theme-dark {
    color-scheme: dark;
    --brand-aco: #7FB8CF;
    --brand-aco-claro: #A3D0E0;
    --brand-aco-profundo: #4A8BA8;
    --brand-grafite-azul: #0A1217;

    --color-bg: var(--brand-grafite-azul);
    --color-bg-soft: #0D171D;
    --color-surface: #13222D;
    --color-surface-strong: #1F3340;
    --color-text: #E3EEF3;
    --color-text-body: #9FB9C6;
    --color-text-muted: #6E8C9B;
    --color-border: rgba(127, 184, 207, 0.12);
    --color-border-strong: #274151;
    --color-accent: var(--brand-aco);
    --color-accent-bright: var(--brand-aco-claro);
    --color-on-accent: #0A1217;
    --color-button-bg: var(--brand-aco);
    --color-button-text: #0A1217;
    --color-success: #30D08D;
    --color-warning: #E5B567;
    --color-danger: #FF6B7A;
    --color-info: #7FB8CF;
    --shadow-soft: 0 12px 32px rgba(0, 0, 0, 0.45);
    --shadow-card: 0 18px 48px rgba(0, 0, 0, 0.55);
}
```

Efeitos exclusivos do tema escuro ficam no fim de `static/css/v2.css` (bloco "Tema dark — mesma paleta do SIGE") e em `static/css/pages/home-v3.css` (home).

**Regra de ouro do CSS:** nunca escreva HEX direto em componentes — use sempre os tokens (`var(--color-...)`). Assim o tema claro e o escuro funcionam juntos sem esforço.

---

## 5. Tipografia

**Família oficial: Inter** (Google Fonts) — pesos 400, 500, 600 e 700.
Alternativas: Segoe UI (Power BI e Office) ou Arial.

**Fonte de números: IBM Plex Mono** (pesos 400 e 500), estilo planilha, usada nos números e rótulos do painel da home (DRE e caixa projetado). Carregada junto com a Inter em `templates/base.html`.

### 5.1 Site

| Elemento | Estilo | Cor (light) |
|---|---|---|
| Título da página (H1) | Inter Medium · 34–54 px · entrelinha 1,08 | Petróleo |
| Título da seção (H2) | Inter Medium · 28–40 px | Petróleo |
| Título de card (H3) | Inter Medium · 19 px | Petróleo |
| Texto | Inter Regular · 16 px · entrelinha 1,65 | Grafite |
| Rótulo de seção (`.eyebrow`) | Inter Medium · 11 px · CAIXA ALTA · espaçamento 1,2 px | Laranja de texto |

### 5.2 Documentos e relatórios

| Elemento | Estilo | Cor |
|---|---|---|
| Título | Inter Bold · 28–32 pt | Petróleo |
| Subtítulo | Inter SemiBold · 16–18 pt | Grafite |
| Texto | Inter Regular · 10–12 pt | Grafite |
| Legenda e fonte | Inter SemiBold · 8–9 pt · CAIXA ALTA | Cinza `#6B6B6B` |

---

## 6. Espaçamento, cantos e sombras

| Item | Valor |
|---|---|
| Escala de espaço | múltiplos de 4 px (`--space-1` = 4 px … `--space-24` = 96 px) |
| Cantos | cards 12 px (`--radius-lg`) · botões 8 px (`--radius-md`) · faixas e imagens 20 px (`--radius-xl`) · selos 999 px |
| Bordas | 1 px `--color-border`; card em destaque com borda laranja |
| Sombras | só no hover e no item em destaque (`--shadow-soft`, `--shadow-card`) |
| Largura máxima do conteúdo | 1200 px (`--container-xl`) |

---

## 7. Componentes do site (`static/css/v2.css`)

### 7.1 Botões

| Classe | Uso |
|---|---|
| `.btn .btn--primary` | Ação principal — **no máximo 1 por seção**. Laranja `#A9561A` no claro, bege-dourado no escuro (tokens `--color-button-*`) |
| `.btn .btn--secondary` | Ação alternativa |
| `.btn .btn--whatsapp` | Abrir conversa no WhatsApp (verde `#1FAA52`) |
| `.site-nav__cta` | Botão "Diagnóstico gratuito" no menu |
| `.whatsapp-float` | Botão flutuante em todas as páginas (`templates/base.html`) |

```html
<a class="btn btn--primary" href="{{ WA_DIAGNOSTICO }}" target="_blank" rel="noopener noreferrer">Agendar diagnóstico gratuito</a>
<a class="btn btn--secondary" href="#solucoes">Conhecer nossas soluções</a>
```

Links de WhatsApp vêm de variáveis globais (`apps/pages/context_processors.py`): `WA_GERAL`, `WA_DIAGNOSTICO`, `WHATSAPP_NUMERO`, `EMAIL_CONTATO`, `LINKEDIN_URL`.

### 7.2 Estrutura de seção

```html
<section class="v2-section [v2-section--soft]" aria-labelledby="x-title">
    <div class="v2-container">
        <div class="v2-head [v2-head--center]">
            <p class="eyebrow text-accent">Rótulo</p>
            <h2 id="x-title">Título da seção</h2>
            <p>Subtítulo opcional.</p>
        </div>
        <div class="v2-grid v2-grid--3"> … cards … </div>
    </div>
</section>
```

Alterne seções normais e `v2-section--soft` para criar ritmo. Grades: `v2-grid--2`, `--3`, `--4` (viram 2 colunas abaixo de 960 px e 1 coluna abaixo de 640 px).

### 7.3 Cards

| Tipo | Classes | Quando usar |
|---|---|---|
| **Dor** | `.v2-card` + `.v2-card__icon` | Problema do cliente: ícone + título + 1 frase. Grade de 4 |
| **Pilar / Pacote** | `.v2-card .v2-card--pillar` + `.v2-list` + `.v2-link` | Serviço ou pacote com lista de entregas |
| **Destaque** | `+ .v2-card--featured` | Só no item recomendado (1 por grade) |
| **Case** | `.v2-card .v2-case` + `.v2-case__media` + `.v2-case__body` + `<dl>` | Desafio → O que foi feito → Resultado |
| **Passo** | `<ol class="v2-steps">` + `<li class="v2-card v2-step">` | Processo numerado (sempre 3 passos) |
| **Selo** | `.v2-badge` | "Dados ilustrativos", "Exemplo de entrega" |
| **Faixa de CTA** | `.v2-cta` + `.v2-cta__actions` | Fechamento de toda página (petróleo no claro, superfície grafite-azulada com brilho azul-aço no escuro) |
| **Sobre** | `.v2-about` + `.v2-avatar` | Bloco com foto e apresentação do consultor |

```html
<article class="v2-card v2-card--pillar v2-card--featured">
    <p class="eyebrow">Mais procurado</p>
    <h3>DRE Gerencial + Fluxo de Caixa</h3>
    <ul class="v2-list">
        <li>Estruturação do fluxo de caixa projetado</li>
        <li>DRE gerencial e margem de contribuição</li>
    </ul>
    <a class="v2-link" href="…">Quero organizar meu financeiro →</a>
</article>
```

---

## 8. Imagens

- Formato **WebP**, largura máxima 1600 px, meta de até 200 KB por imagem.
- Sempre `width`, `height` e `alt` descritivo; `loading="lazy"` abaixo da primeira dobra.
- Prints de dashboard com dados fictícios levam o selo **"Dados ilustrativos"**.
- Cases nunca exibem números inventados como se fossem reais.
- Foto do consultor: `static/img/sobre/leles.webp` (retrato 4:5, fundo neutro).

---

## 9. Relatórios, apresentações e dashboards (Power BI)

**Padrão de documento**
1. Capa com logo, título e data
2. Títulos em negrito petróleo, texto em grafite
3. Tabelas com cabeçalho petróleo e linhas alternadas em bege
4. Um destaque em laranja por página, no máximo
5. Valores negativos em vermelho
6. Fonte dos dados no rodapé

**Dashboards:** fundo bege, cabeçalho petróleo, cards brancos com cantos arredondados, números grandes em Inter Bold.

**Ordem das cores nas séries:** `#17545E` → `#E0812F` → `#5E8F96` → `#C9B99A`.
Laranja só para o dado que merece atenção · vermelho (`#C2553D`) só para queda ou alerta · barras retas, sem 3D e sem sombra.

**Tema Power BI (JSON) sugerido:**

```json
{
  "name": "ServicesBI 2026",
  "dataColors": ["#17545E", "#E0812F", "#5E8F96", "#C9B99A", "#2B2B2B", "#A9561A", "#8FB3B8", "#E7DCC7"],
  "background": "#FFFFFF",
  "foreground": "#2B2B2B",
  "tableAccent": "#17545E",
  "good": "#2E7D4F",
  "neutral": "#B7791F",
  "bad": "#C2553D",
  "maximum": "#17545E",
  "center": "#E7DCC7",
  "minimum": "#E0812F"
}
```

---

## 10. Tom de voz

| Atributo | Assim sim | Assim não |
|---|---|---|
| **Direta** — vai ao ponto e mostra o número | "A margem caiu 4 pontos em março por causa do frete." | "Observou-se uma variação negativa nos indicadores de rentabilidade." |
| **Clara** — o empresário entende sem glossário | "Em 60 dias vai faltar R$ 40 mil no caixa se nada mudar." | "O pipeline ETL alimenta o modelo DAX com granularidade diária." |
| **Próxima** — lado a lado, sem perder a seriedade | "Separei três ajustes que liberam caixa já neste mês." | "Seguem, conforme solicitado, as recomendações pertinentes." |
| **Confiante** — recomenda sem exagerar | "Recomendo revisar o preço da linha D antes de investir em vendas." | "Vamos triplicar seu lucro em 30 dias!" |

**No site:** a home fala de negócio (caixa, margem, lucro). Termos técnicos — Python, DAX, APIs, n8n — ficam nas páginas internas.

---

## 11. Checklist para uma página nova

- [ ] Estende `base.html`; `title`, `meta_description` e `og_title` próprios
- [ ] Um único H1; seções com `aria-labelledby`
- [ ] Só tokens de cor (nenhum HEX solto); testada nos temas claro **e** escuro
- [ ] No máximo 1 botão primário por seção; termina com faixa `.v2-cta`
- [ ] Imagens em WebP com `alt`, `width`, `height`
- [ ] Texto revisado pelo tom de voz (seção 10)
- [ ] Rota adicionada em `apps/pages/urls.py`, em `PAGINAS_PUBLICAS` (`views.py`) e no `export_static_site`
- [ ] `python manage.py export_static_site` sem erro; conferida no celular (390 px)

## 12. Ao pedir alterações a uma IA (Claude, Codex)

> "Siga `docs/SERVICESBI_IDENTIDADE_VISUAL.md`. Use apenas tokens de `tokens.css` e componentes de `v2.css`. Não crie cores novas. Teste nos temas claro e escuro e no celular."

---

## 13. Decisões de design registradas (histórico das conversas, nov/2026)

**Posicionamento visual**
- A ServicesBI é uma **consultoria financeira** respaldada por dados, BI e automação. O visual tem que parecer finanças, não "fábrica de software" e não "cara de IA".
- O visitante deve perceber em segundos que o Leles "sabe fazer as coisas": o topo da home mostra uma **DRE gerencial** e um **caixa projetado de 12 semanas** com a semana 7 abaixo do mínimo (dados ilustrativos, com selo).
- Menos cards e mais respiro. Dores em lista numerada, cases em tabela.

**Home e páginas**
- A home aprovada é o **"Modelo B ajustado"** (18/11/2026). Seções: topo com DRE e caixa → faixa de credenciais reais → 01 Diagnóstico (dores) → 02 Método (3 pilares) → 03 Ferramentas ServicesBI (SIGE, Automações, Modelos financeiros, Jarvis, com selo de status) e Novidades → 04 Cases → 05 Quem conduz → 06 Como trabalhamos (escada de ofertas) → material gratuito → chamada final.
- A **home é a página de Consultoria Financeira**: o item "Consultoria Financeira" do menu abre a home.
- A home é o **modelo para todas as páginas**: cada página nova parte da estrutura dela e depois é moldada para o seu assunto.
- **Alinhamento:** todas as seções de todas as páginas seguem as margens laterais do hero da home.
- Menu atual: **Consultoria Financeira · BI & Dashboards · Nossos Produtos · Cases · Sobre**, mais o botão "Diagnóstico gratuito". O "Currículo" fica dentro de "Sobre".
- Rodapé com redes sociais (LinkedIn, Instagram, GitHub, WhatsApp).
- Nada de números inventados apresentados como reais; prints de dashboards são **provisórios** (serão refeitos) e levam o selo "Dados ilustrativos".

**Produtos e marca nos sistemas**
- Produtos iniciais: **SIGE, Jarvis, Automações n8n e Excel corporativo**. Continuam no marketing, como diferencial, sem tirar o foco do financeiro.
- O **SIGE é uma extensão do site**: segue a mesma identidade (paleta e fontes). A capa/login do SIGE foi refeita com a paleta e as fontes do site 2.0, e o dark do site agora é o mesmo do SIGE.
- Todo sistema aberto no navegador (SIGE, Jarvis, Compras, outros) leva o **favicon da ServicesBI** (seção 2).

**Pendências visuais**
- [ ] Logo do tema escuro ainda é violeta: gerar versão em azul-aço.
- [ ] Favicon e imagem de compartilhamento ainda usam o logo original azul e verde.
- [ ] Foto profissional em `static/img/sobre/leles.webp` (enquanto não existir, aparece "LJ").
- [ ] Refazer os dashboards Power BI exibidos no site.
- [ ] Novidades reais das ferramentas para ativar a seção da home.

**Forma de trabalhar**
- Mudança grande: primeiro um **esboço para aprovação**, só depois mexer no site.
- Testar sempre nos temas claro e escuro e no celular (390 px).
- Commit e publicação só no final, quando o Leles pedir.
