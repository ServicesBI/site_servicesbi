# ServicesBI — Paleta de Cores Oficial

> **Fonte de verdade visual do projeto.**
> Qualquer alteração de cor, criação de novo componente ou revisão de identidade deve consultar este documento antes de ser aplicada ao código.

---

## 1. Objetivo

Este arquivo define e documenta a paleta oficial de cores do site ServicesBI (Dados, BI e Automações). Ele serve como referência visual autoritativa para designers, desenvolvedores e qualquer colaborador que precise tomar decisões visuais no projeto.

As cores aqui listadas foram extraídas diretamente dos arquivos CSS existentes — nenhuma cor foi inventada ou extrapolada. O documento deve ser mantido atualizado sempre que novos tokens forem criados ou cores existentes forem alteradas em `tokens.css`.

**Identidade visual em resumo:**
- **Tema Light:** fundo creme quente, textos quase-pretos, accent vermelho-laranja (`#CA3A18`) que remete a energia e precisão.
- **Tema Dark:** base azul-marinha profundo, texto gelo claro, accent ciano vibrante (`#38CBD9`) que remete a tecnologia e dados.

---

## 2. Arquivos analisados

| Arquivo | Função |
|---|---|
| `static/css/tokens.css` | Definição central de todos os design tokens (cores, tipografia, espaçamento, sombras) |
| `static/css/base.css` | Reset, estilos globais de HTML, body, links, headings, utilitários de texto |
| `static/css/buttons.css` | Variantes de botão (primary, secondary, ghost, link, sm, lg) |
| `static/css/cards.css` | Variantes de card (soft, strong, interactive) e subcomponentes |
| `static/css/footer.css` | Layout e cores do rodapé do site |
| `static/css/header.css` | Header fixo, logo, nav, tema-toggle |
| `static/css/layout.css` | Containers, sections, grids globais |
| `static/css/pages/home.css` | Hero, robot stage, solutions, Jarvis carousel, portfólio |
| `static/css/pages/powerbi.css` | Hero da página Power BI |
| `static/css/pages/automacoes.css` | Hero da página Automações |
| `static/css/pages/excel.css` | Hero da página Excel |
| `static/css/pages/python.css` | Hero, service hero base, projetos Python |

---

## 3. Tema Light

O tema Light é ativado por padrão (`:root` com `color-scheme: light`). Fundo quente levemente off-white, texto quase-preto com tom esverdeado, accent vermelho-tijolo.

| Token CSS | Valor | Função visual | Onde aparece / uso provável |
|---|---|---|---|
| `--color-bg` | `#FFFFFB` | Fundo principal da página | `html`, `body`, `main`, `.section`, `.section-hero` |
| `--color-bg-soft` | `#FAFAF7` | Fundo alternado suave | `.section--soft`, cards `.card--soft`, footer, `.home-solutions` |
| `--color-surface` | `#FAFAF7` | Superfície de componentes (cards, inputs) | `.card`, `.btn--secondary`, `.home-solution-card` |
| `--color-surface-strong` | `#FFFFFF` | Superfície com maior contraste | `.card--strong`, modal, overlays que precisam de destaque |
| `--color-text` | `#1A1A18` | Texto primário (títulos, headings) | `h1`, `h2`, `h3`, `.section-title`, `.card__title` |
| `--color-text-body` | `#505C57` | Texto de corpo / parágrafos | `body`, `p`, `.card__text`, nav links, `.site-footer__nav a` |
| `--color-text-muted` | `#717A76` | Texto secundário / metadados | `.text-muted`, `.card__meta`, `.site-footer__meta`, `.service-hero__points` |
| `--color-border` | `#E5E5E5` | Borda padrão de componentes | Cards, inputs, header bottom, footer top, `.btn--ghost` |
| `--color-border-strong` | `#D4D4D4` | Borda com maior contraste (hover, focus) | `.card--strong`, hover states de cards e botões |
| `--color-accent` | `#CA3A18` | Cor de destaque principal (vermelho-laranja) | Botões primários, links hover, `.site-logo span`, `.card__eyebrow`, `.card__icon`, bullet spotlight |
| `--color-success` | `#10B981` | Feedback positivo / status OK | Badges de status, mensagens de sucesso |
| `--color-warning` | `#F59E0B` | Alerta / atenção | Badges de aviso, notificações amarelas |
| `--color-danger` | `#DC2626` | Erro / ação destrutiva | Formulários com erro, alertas críticos |
| `--color-info` | `#3B82F6` | Informação / destaque neutro | Tooltips, Jarvis card glow accent, info badges |
| `--shadow-soft` | `0 12px 32px rgba(26,26,24,0.08)` | Sombra suave para elevação leve | `.card`, `.home-solution-card`, `.home-portfolio__filters` |
| `--shadow-card` | `0 18px 48px rgba(26,26,24,0.12)` | Sombra mais intensa para cards fortes | `.card--strong`, hover interativos |

---

## 4. Tema Dark

O tema Dark é ativado pela classe `html.theme-dark` ou `body.theme-dark`. Todos os tokens de cor são sobrescritos mantendo os mesmos nomes.

| Token CSS | Valor | Função visual | Onde aparece / uso provável |
|---|---|---|---|
| `--color-bg` | `#0A1420` | Fundo principal escuro (azul-marinha profundo) | `html`, `body`, `main`, `.section` |
| `--color-bg-soft` | `#112236` | Fundo alternado ligeiramente mais claro | `.section--soft`, footer, gradientes de seção |
| `--color-surface` | `#112236` | Superfície de componentes no dark | `.card`, `.btn--secondary`, header backdrop |
| `--color-surface-strong` | `#1A2F4A` | Superfície com destaque | `.card--strong`, modais |
| `--color-text` | `#F5F9FC` | Texto primário (quase branco com tom gelo) | `h1`, `h2`, `h3`, `.section-title` |
| `--color-text-body` | `#B8C9DC` | Texto de corpo (azul-gelo suave) | `body`, `p`, `.card__text`, nav links |
| `--color-text-muted` | `#8A9BAA` | Texto secundário / metadados | `.text-muted`, `.card__meta`, `.service-hero__points` |
| `--color-border` | `rgba(255,255,255,0.10)` | Borda sutil (branco translúcido 10%) | Cards, header, footer, inputs |
| `--color-border-strong` | `rgba(255,255,255,0.16)` | Borda com maior contraste (16% branco) | `.card--strong`, hover states |
| `--color-accent` | `#38CBD9` | Cor de destaque principal (ciano vibrante) | Botões primários, links hover, logo span, eyebrows, bullet spots |
| `--color-success` | `#30D08D` | Feedback positivo | Badges, mensagens de sucesso |
| `--color-warning` | `#F2C94C` | Alerta / atenção | Badges de aviso |
| `--color-danger` | `#FF6B7A` | Erro / ação destrutiva | Formulários com erro, alertas críticos |
| `--color-info` | `#65A9EA` | Informação / destaque neutro | Tooltips, Jarvis glow, info badges |
| `--shadow-soft` | `0 12px 32px rgba(0,0,0,0.28)` | Sombra suave (mais intensa que no light) | `.card`, componentes elevados |
| `--shadow-card` | `0 18px 48px rgba(0,0,0,0.36)` | Sombra forte para cards | `.card--strong`, hover interativos |

---

## 5. Tokens globais de cor

Todos os tokens de cor definidos em `tokens.css`, com valores em ambos os temas:

| Token | Valor Light | Valor Dark | Categoria |
|---|---|---|---|
| `--color-bg` | `#FFFFFB` | `#0A1420` | Fundos |
| `--color-bg-soft` | `#FAFAF7` | `#112236` | Fundos |
| `--color-surface` | `#FAFAF7` | `#112236` | Superfícies |
| `--color-surface-strong` | `#FFFFFF` | `#1A2F4A` | Superfícies |
| `--color-text` | `#1A1A18` | `#F5F9FC` | Tipografia |
| `--color-text-body` | `#505C57` | `#B8C9DC` | Tipografia |
| `--color-text-muted` | `#717A76` | `#8A9BAA` | Tipografia |
| `--color-border` | `#E5E5E5` | `rgba(255,255,255,0.10)` | Bordas |
| `--color-border-strong` | `#D4D4D4` | `rgba(255,255,255,0.16)` | Bordas |
| `--color-accent` | `#CA3A18` | `#38CBD9` | Accent |
| `--color-success` | `#10B981` | `#30D08D` | Semântica |
| `--color-warning` | `#F59E0B` | `#F2C94C` | Semântica |
| `--color-danger` | `#DC2626` | `#FF6B7A` | Semântica |
| `--color-info` | `#3B82F6` | `#65A9EA` | Semântica |
| `--shadow-soft` | `0 12px 32px rgba(26,26,24,0.08)` | `0 12px 32px rgba(0,0,0,0.28)` | Sombras |
| `--shadow-card` | `0 18px 48px rgba(26,26,24,0.12)` | `0 18px 48px rgba(0,0,0,0.36)` | Sombras |

**Total: 16 tokens de cor/sombra definidos centralmente.**

---

## 6. Cores por componente

### Header (`header.css`)

O header usa `color-mix()` para criar um backdrop translúcido que combina com o fundo da página em ambos os temas.

| Propriedade | Token utilizado |
|---|---|
| Fundo (92% opaco + blur) | `color-mix(in srgb, var(--color-bg) 92%, transparent)` |
| Borda inferior | `--color-border` |
| Cor do logo | `--color-text` (texto) + `--color-accent` (span colorido) |
| Links de navegação | `--color-text-body` (normal) / `--color-accent` (hover e active) |
| Botão theme-toggle | `--color-text`, `color-mix(--color-surface 68%, transparent)`, `--color-border` |
| Hover do theme-toggle | `--color-border-strong`, `--shadow-soft` |

### Footer (`footer.css`)

| Propriedade | Token utilizado |
|---|---|
| Fundo | `--color-bg-soft` |
| Borda superior | `--color-border` |
| Texto principal | `--color-text-muted` |
| Links de navegação | `--color-text-body` (normal) / `--color-accent` (hover) |
| Metadados / copyright | `--color-text-muted` |

### Botões (`buttons.css`)

| Variante | Tokens de cor utilizados |
|---|---|
| `.btn--primary` | Fundo/borda: `--color-accent` · Texto: `--color-bg` · Sombra: `color-mix(--color-accent 18-22%, transparent)` |
| `.btn--secondary` | Fundo: `--color-surface` · Texto: `--color-text` · Borda: `--color-border` · Hover sombra: `--shadow-soft` |
| `.btn--ghost` | Fundo: transparente · Texto: `--color-text` · Borda: `--color-border` · Hover texto/borda: `--color-accent` / `--color-border-strong` |
| `.btn--link` | Texto: `--color-accent` · Hover texto: `--color-text` |
| Estado disabled | Texto: `--color-text-muted` · Fundo: `--color-bg-soft` · Borda: `--color-border` |
| Focus outline | `--color-accent` (2px solid) |

### Cards (`cards.css`)

| Variante / Elemento | Tokens de cor utilizados |
|---|---|
| `.card` (base) | Fundo: `--color-surface` · Texto: `--color-text-body` · Borda: `--color-border` · Sombra: `--shadow-soft` |
| `.card--soft` | Fundo: `--color-bg-soft` · Sem sombra |
| `.card--strong` | Fundo: `--color-surface-strong` · Borda: `--color-border-strong` · Sombra: `--shadow-card` |
| `.card--interactive` (hover) | Borda: `--color-border-strong` · Sombra: `--shadow-soft` |
| `.card--interactive::after` (barra accent) | `--color-accent` |
| `.card__icon` | Cor do ícone: `--color-accent` · Fundo: `--color-bg-soft` · Borda: `--color-border` |
| `.card__eyebrow` | `--color-accent` |
| `.card__title` | `--color-text` |
| `.card__text` | `--color-text-body` |
| `.card__meta` | `--color-text-muted` |
| `.card__footer` | Borda top: `--color-border` |

### Layout global (`layout.css`)

| Elemento | Tokens de cor utilizados |
|---|---|
| `main`, `.section` | Fundo: `--color-bg` |
| `.section--soft` | Fundo: `--color-bg-soft` |
| `.section-title` | `--color-text` |
| `.section-subtitle` | `--color-text-body` |

### Páginas específicas

**Home (`home.css`)**

A página home define variáveis locais adicionais para o robô Spline e para o carrossel Jarvis:

| Variável local | Valor Light | Valor Dark | Uso |
|---|---|---|---|
| `--home-robot-tint` | `#c2ac98` (hardcoded) | `#081724` (hardcoded) | Tint aplicado via `color-mix` + `mix-blend-mode` sobre o viewer Spline |
| `--home-robot-tint-opacity` | `0.56` | `0.78` | Opacidade do overlay de tint |
| `--jarvis-bg` | `color-mix(--color-text 86%, --color-bg 14%)` | `--color-bg` | Fundo dos cards Jarvis |
| `--jarvis-surface` | `color-mix(--color-text 78%, transparent)` | `color-mix(--color-surface 68%, transparent)` | Superfície dos cards Jarvis |
| `--jarvis-text` | `--color-bg` | `--color-text` | Texto dentro dos cards Jarvis |
| `--jarvis-text-soft` | `color-mix(--color-bg 72%, --color-text-muted)` | `--color-text-body` | Texto secundário Jarvis |

Gradientes de seção (compostos de tokens):

- **Hero stage:** `radial-gradient(accent 18%, transparent)` + `linear-gradient(--color-bg → --color-bg-soft → --color-surface)`
- **Home Solutions:** `radial-gradient(accent 10%, transparent)` + `linear-gradient(--color-bg → --color-bg-soft)`
- **Home Portfolio:** `radial-gradient(accent 12%, transparent)` + `linear-gradient(--color-bg-soft → --color-bg)`

**Páginas de serviço (powerbi, automacoes, excel, python)**

Todas as páginas de serviço reusam o padrão `.service-hero` definido em `python.css`:

- Fundo do hero: mesmo gradiente da home (accent radial + linear bg/bg-soft/surface)
- Bullet points do hero: `--color-accent` com `box-shadow: 0 0 18px color-mix(--color-accent 70%, transparent)`
- Links de seção: `--color-accent` / hover `color-mix(--color-accent 82%, --color-text)`
- `.python-project__cta`: estilo de `.btn--primary` (accent fundo, bg texto)

---

## 7. Cores hardcoded encontradas fora do `tokens.css`

As seguintes cores foram encontradas escritas diretamente no CSS, fora do arquivo de tokens:

| # | Arquivo | Seletor / contexto | Cor encontrada | Recomendação |
|---|---|---|---|---|
| 1 | `pages/home.css` | `:root { --home-robot-tint }` | `#c2ac98` | **Manter como local token** — cor de tint específica do robô Spline; não faz sentido como token global. Considerar documentar como token de página. |
| 2 | `pages/home.css` | `html.theme-dark { --home-robot-tint }` | `#081724` | **Manter como local token** — idem ao item 1; cor de tint dark do robô Spline. |
| 3 | `pages/home.css` | `:root { --home-robot-filter: drop-shadow(...) }` | `color-mix(in srgb, #c2ac98 28%, transparent)` | **Manter** — parte do filtro CSS do robô Spline, depende do valor `#c2ac98` acima. |
| 4 | `pages/home.css` | `html.theme-dark { --home-robot-filter: drop-shadow(...) }` | `color-mix(in srgb, #081724 42%, transparent)` | **Manter** — idem ao item 3 para o modo dark. |
| 5 | `pages/python.css` | `.python-projects__list > .python-project:first-child .python-project__media` | `#080d18` | **Avaliar migração** — fundo da mídia do card Jarvis (1º projeto Python). Poderia ser substituído por `var(--color-bg)` no dark theme ou tornar-se um token de página como `--python-jarvis-bg`. |

**Total de cores hardcoded fora de tokens.css: 5 ocorrências (3 valores únicos).**

> **Nota:** Todos os usos de `color-mix()`, `rgba()` e `transparent` que referenciam `var(--color-*)` nos outros arquivos CSS **não são hardcoded** — são derivações de tokens e estão corretos.

---

## 8. Regras oficiais de uso

As regras abaixo devem orientar qualquer trabalho visual no projeto ServicesBI:

**8.1 — Criação de novas cores**
Toda nova cor deve ser criada como um token CSS em `tokens.css`, com valores definidos para `:root` (light) e `html.theme-dark` (dark). Nunca inserir valores hexadecimais ou `rgb()` diretamente em arquivos de componentes.

**8.2 — Consumo de tokens**
Componentes devem sempre referenciar tokens via `var(--color-*)`. O uso de hex direto em componentes é permitido apenas como exceção documentada (ex.: tints visuais específicos de ilustrações, como os da seção do robô).

**8.3 — Botão primário**
O botão primário usa `--color-accent` como fundo. A sombra deve ser gerada via `color-mix(in srgb, var(--color-accent) 18-22%, transparent)` para manter leveza visual. Não usar sombras fixas em hex.

**8.4 — Cards interativos**
Cards interativos devem seguir o padrão: borda `--color-border` (normal) → `--color-border-strong` (hover), sombra `--shadow-soft`, barra accent `--color-accent` no bottom via `::after`. Não inventar sombras coloridas fora desse padrão.

**8.5 — Contraste light/dark**
Os temas light e dark têm identidades visuais distintas:
- Light: fundo quente off-white, accent vermelho-laranja, texto quase-preto.
- Dark: fundo azul-marinha profundo, accent ciano, texto gelo/azulado.
Nunca "espelhar" um tema no outro sem revisão visual.

**8.6 — Gradientes de seção**
Gradientes devem ser compostos exclusivamente de tokens de cor via `var()` ou `color-mix()` com tokens. Não usar hex em gradientes de seção.

**8.7 — Identidade de marca**
Não criar cores fora do espectro de identidade ServicesBI (quente-terroso no light, azul-ciano no dark) sem revisar este documento e obter aprovação.

---

## 9. Recomendações de padronização

As inconsistências e oportunidades de melhoria abaixo foram identificadas na análise. **Nenhuma alteração foi aplicada** — estas são sugestões para versões futuras:

**9.1 — `#080d18` em `python.css` (prioridade média)**
O fundo `#080d18` do card Jarvis poderia ser substituído por `var(--color-bg)` (que no dark é `#0A1420`, muito próximo) ou transformado em token de página `--python-jarvis-bg`. Benefício: manutenção centralizada ao alterar o fundo dark.

**9.2 — `--home-robot-tint` como token de página formal**
As variáveis `--home-robot-tint`, `--home-robot-tint-opacity`, `--home-robot-tint-blend-mode` e `--home-robot-filter` são tokens locais bem estruturados dentro de `home.css`. Estão bem organizados, mas seria interessante adicionar um comentário explícito de que são tokens de escopo de página, para distingui-los dos tokens globais de `tokens.css`.

**9.3 — Ausência de token de cor para `--color-accent-muted`**
Vários componentes usam `color-mix(in srgb, var(--color-accent) 10-26%, transparent)` diretamente para criar fundos e bordas de badges/tags. Um token dedicado como `--color-accent-subtle` (ex.: `color-mix(in srgb, var(--color-accent) 12%, transparent)`) reduziria a repetição e padronizaria o peso visual desses elementos.

**9.4 — Sombras de botão primário com valores levemente diferentes**
Em `buttons.css`, a sombra do `.btn--primary` usa 18% e no hover 22% do accent. Em `python.css` (`.python-project__cta`), os valores são 22% e 28%. Seria útil definir tokens `--shadow-btn-primary` e `--shadow-btn-primary-hover` em `tokens.css` para unificar.

**9.5 — Verificar se `--color-surface` e `--color-bg-soft` devem ser distintos**
No tema light, ambos possuem o mesmo valor (`#FAFAF7`). Isso é intencional e funciona corretamente, pois permitem semânticas diferentes (superfície de componente vs. fundo de seção alternado). Manter a distinção semântica mesmo que os valores coincidam.

---

## 10. Resumo executivo

| Papel visual | Light | Dark |
|---|---|---|
| **Cor base de fundo** | `#FFFFFB` (`--color-bg`) | `#0A1420` (`--color-bg`) |
| **Cor de superfície/card** | `#FAFAF7` (`--color-surface`) | `#112236` (`--color-surface`) |
| **Accent principal** | `#CA3A18` — vermelho-laranja | `#38CBD9` — ciano vibrante |
| **Texto primário (títulos)** | `#1A1A18` (`--color-text`) | `#F5F9FC` (`--color-text`) |
| **Texto de corpo** | `#505C57` (`--color-text-body`) | `#B8C9DC` (`--color-text-body`) |
| **Borda padrão** | `#E5E5E5` (`--color-border`) | `rgba(255,255,255,0.10)` (`--color-border`) |
| **Sombra padrão** | `rgba(26,26,24,0.08)` | `rgba(0,0,0,0.28)` |

**Tokens definidos em `tokens.css`: 16**
**Cores hardcoded fora de `tokens.css`: 5 ocorrências (3 valores únicos)**
**Arquivos CSS analisados: 12**
**Arquivos CSS alterados: 0**
