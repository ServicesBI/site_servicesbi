# ServicesBI — Guia de Identidade Visual (v2026)

> **Fonte de verdade da marca ServicesBI.** Versão técnica do *Manual de Identidade Visual* (PDF).
> Vale para o site, propostas, relatórios, apresentações e dashboards em Power BI.
> Substitui `SERVICESBI_COLOR_PALETTE.md` (paleta antiga com accent `#CA3A18`).

---

## 1. Essência da marca

**Quem somos:** consultoria financeira que usa análise de dados, Business Intelligence e automação para organizar, controlar e fazer crescer pequenas e médias empresas.

**O que a identidade precisa transmitir:** clareza · precisão · confiança · proximidade.

---

## 2. Logo

| Arquivo | Uso |
|---|---|
| `static/img/brand/logo-servicesbi.png` | Símbolo redondo, fundo transparente (410×410 px) |
| `static/img/brand/favicon.ico` / `favicon-32.png` | Aba do navegador |
| `static/img/brand/apple-touch-icon.png` | Atalho no iPhone (fundo escuro) |
| `static/img/brand/icon-512.png` | Dados estruturados (Google), redes sociais |
| `static/img/brand/og-servicesbi.png` | Imagem de compartilhamento (WhatsApp, LinkedIn) 1200×630 |

**Assinatura em texto** (cabeçalho do site e documentos): `Services` na cor do título + `BI` na cor de destaque da marca (laranja `#E0812F` no claro, violeta `#8B5CFF` no escuro).

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

Estilo **premium**: fundo quase preto, brilho violeta, cards em roxo profundo e botões bege-dourados. O bege dos botões faz a ponte com o fundo bege do tema claro.

### 4.1 Cores

| Nome | HEX | Uso |
|---|---|---|
| **Preto-azulado** | `#06060E` | Fundo |
| Superfície suave | `#0E0E18` | Seções alternadas |
| Superfície | `#161624` | Painéis |
| Superfície forte | `#1E1B33` | Cards (com degradê `#2A2150 → #1A1830 → #161624`) |
| Branco-lavanda | `#F5F4FA` | Títulos |
| Lavanda-acinzentado | `#C9C8DA` | Texto |
| Cinza-lavanda | `#8E8DA8` | Texto secundário |
| **Violeta** | `#7335FD` | Preenchimentos, brilhos, números de passo, borda do card em destaque |
| Violeta de títulos | `#8B5CFF` | Títulos de seção (H2) e "BI" da assinatura em texto |
| Violeta de texto | `#9B7BFF` | Links, rótulos e destaques em texto (contraste 6,4:1) |
| **Bege-dourado** | `#E8C9A0` | Botões de ação (degradê `#F1D9B8 → #DDBB90`, texto `#1A1428`) |
| Coral | `#FF6B7A` | Alertas |

> **Regra:** violeta `#7335FD` só **preenchendo áreas** (com texto branco) · em **texto** use `#9B7BFF` ou `#8B5CFF` (títulos grandes) · **botão de ação** sempre bege-dourado.

**Correspondência entre os temas:** fundo bege → preto-azulado · títulos petróleo → branco-lavanda (seções em violeta) · texto grafite → lavanda-acinzentado · destaque laranja → violeta · botão laranja → bege-dourado.

### 4.2 Tokens CSS (dark)

```css
html.theme-dark, body.theme-dark {
    --brand-violeta: #7335FD;
    --brand-dourado: #E8C9A0;
    --brand-preto: #06060E;

    --color-bg: var(--brand-preto);
    --color-bg-soft: #0E0E18;
    --color-surface: #161624;
    --color-surface-strong: #1E1B33;
    --color-text: #F5F4FA;
    --color-text-body: #C9C8DA;
    --color-text-muted: #8E8DA8;
    --color-border: rgba(255, 255, 255, 0.08);
    --color-border-strong: rgba(155, 123, 255, 0.28);
    --color-accent: #9B7BFF;
    --color-accent-bright: #8B5CFF;
    --color-on-accent: #FFFFFF;
    --color-button-bg: var(--brand-dourado);
    --color-button-text: #1A1428;
    --color-danger: #FF6B7A;
}
```

Efeitos exclusivos do tema escuro ficam no fim de `static/css/v2.css` (bloco "Tema dark — estilo premium"): brilho violeta no hero e na faixa de CTA, degradê dos cards, títulos de seção em violeta e botões em degradê bege.

**Regra de ouro do CSS:** nunca escreva HEX direto em componentes — use sempre os tokens (`var(--color-...)`). Assim o tema claro e o escuro funcionam juntos sem esforço.

---

## 5. Tipografia

**Família oficial: Inter** (Google Fonts) — pesos 400, 500, 600 e 700.
Alternativas: Segoe UI (Power BI e Office) ou Arial.

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
| **Faixa de CTA** | `.v2-cta` + `.v2-cta__actions` | Fechamento de toda página (petróleo no claro, roxo-noite `#12102A` com brilho violeta no escuro) |
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
