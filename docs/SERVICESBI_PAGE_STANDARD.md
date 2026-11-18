> ⚠️ **Documento anterior ao ServicesBI 2.0.** Para cores, tipografia e componentes, a referência oficial agora é `docs/SERVICESBI_IDENTIDADE_VISUAL.md` (e o PDF `Manual_Identidade_Visual_ServicesBI.pdf`).

# ServicesBI — Skill de Padronização de Páginas

> **Uso:** este arquivo deve ser usado como regra fixa para qualquer ajuste/criação de página do site ServicesBI.  
> **Objetivo:** evitar improviso visual, desalinhamento entre páginas e retrabalho em Hero, cards, margens, temas e imagens.

---

## 1. Princípio central

A página **Home** é a fonte da verdade visual do site.

Qualquer página nova ou ajuste em páginas existentes deve respeitar a geometria da Home:

- mesma lógica de header;
- mesma altura visual do Hero;
- mesmo alinhamento horizontal do texto principal;
- mesma altura vertical de início da chamada;
- mesma família/tamanho/peso de fonte;
- mesma largura do bloco textual;
- mesmo espaçamento entre eyebrow, título, subtítulo, botões e bullets;
- mesma lógica de container;
- mesma linguagem visual nos cards;
- mesmo comportamento light/dark.

A página específica pode trocar o conteúdo e a imagem, mas **não pode inventar uma nova estrutura visual**.

---

## 2. Regra de ouro

Antes de alterar qualquer página, auditar:

```txt
templates/pages/home.html
static/css/pages/home.css
```

Depois aplicar o equivalente na página de destino.

**Não chutar valores.**  
**Não criar layout novo por interpretação.**  
**Não alterar a Home, salvo pedido explícito.**

---

## 3. Arquivos globais protegidos

Por padrão, não alterar:

```txt
static/css/tokens.css
static/css/base.css
static/css/layout.css
static/css/header.css
static/css/footer.css
static/js/*
templates/pages/home.html
static/css/pages/home.css
```

Só alterar arquivos globais se a tarefa pedir explicitamente.

---

## 4. Estrutura padrão de página

Toda página principal deve seguir esta ordem conceitual:

```txt
1. Hero
2. Seção de áreas/serviços/entregas
3. Seção de projetos/cases/cards
4. Seções específicas da página, se necessário
5. Footer
```

A página pode ter conteúdo diferente, mas o ritmo visual deve permanecer consistente.

---

## 5. Hero — padrão obrigatório

### 5.1 Fonte da verdade

O Hero da Home define:

- altura da seção;
- distância abaixo do header;
- posição do texto;
- largura do texto;
- tamanho do título;
- peso do título;
- espaçamento entre elementos;
- estilo dos botões;
- lógica do elemento visual à direita.

### 5.2 Estrutura conceitual

```html
<section class="page-hero">
    <div class="container">
        <div class="page-hero__inner">

            <div class="page-hero__content">
                <p class="page-hero__eyebrow">CATEGORIA • SUBCATEGORIA</p>

                <h1 class="page-hero__title">
                    Título principal da página
                </h1>

                <p class="page-hero__lead">
                    Texto de apoio com explicação objetiva da entrega.
                </p>

                <div class="page-hero__actions">
                    <!-- botões -->
                </div>

                <ul class="page-hero__bullets">
                    <!-- bullets curtos -->
                </ul>
            </div>

            <div class="page-hero__visual">
                <!-- imagem, robô, ilustração ou background controlado -->
            </div>

        </div>
    </div>
</section>
```

Na prática, cada página pode usar prefixo próprio:

```txt
home-hero__
py-hero__
powerbi-hero__
automacao-hero__
excel-hero__
```

Mas a geometria deve ser equivalente.

---

## 6. Alinhamento obrigatório do texto entre páginas

Quando o usuário navega de Home para Python, Power BI, Automações, Excel etc., o bloco textual do Hero **não pode “pular” de lugar**.

O início visual do texto deve bater com a Home:

```txt
Home:
ServicesBI
Inteligência de dados e automação...

Python:
PYTHON • AUTOMAÇÕES • DADOS
Python aplicado à automação...
```

Devem estar alinhados em:

- eixo X inicial;
- eixo Y inicial;
- largura do bloco;
- espaçamento vertical interno;
- escala tipográfica.

Se a página nova estiver visualmente “bonita”, mas o texto começar em posição diferente da Home, está errado.

---

## 7. Tipografia do Hero

O título do Hero deve seguir a Home.

Antes de mexer, verificar no CSS da Home:

```txt
font-size
font-weight
line-height
letter-spacing
max-width
margin
```

Depois aplicar os mesmos valores equivalentes na página.

### Proibições

Não fazer:

```css
font-size: gigante sem comparação com a Home;
max-width muito estreito;
letter-spacing diferente sem necessidade;
line-height diferente da Home;
padding manual para “ajeitar no olho”;
<br> manual no título, salvo exceção aprovada.
```

### Título

O título deve quebrar naturalmente de forma elegante.  
Evitar títulos quebrando em 4, 5 ou 6 linhas no desktop.

---

## 8. Hero com imagem ou arte visual

### 8.1 Regra

A imagem do Hero **não pode controlar a posição do texto**.

O texto é a camada principal.  
A arte é camada visual.

### 8.2 Quando usar `<img>`

Usar `<img>` apenas se o asset for um objeto isolado ou imagem com fundo transparente/integrado, como:

```txt
robô
ícone 3D isolado
render sem fundo
mockup com transparência real
```

### 8.3 Quando usar background

Usar `background-image` no Hero quando o asset for um banner amplo, com fundo próprio e espaço livre para texto.

Exemplo:

```css
.page-hero::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    background-image: url("../../img/pagina/hero/hero_dark.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
    pointer-events: none;
}
```

### 8.4 Cuidado com `cover`

`background-size: cover` só funciona bem se a imagem for realmente um **banner completo**, com espaço livre planejado para texto.

Se a imagem for apenas uma arte lateral, usar:

```css
background-size: contain;
background-position: right center;
```

e limitar a área visual:

```css
.page-hero::before {
    top: 0;
    right: 0;
    bottom: 0;
    width: min(76vw, 1480px);
}
```

### 8.5 Regra prática

- imagem tipo capa/banner: `cover`;
- imagem tipo objeto/arte lateral: `contain`;
- imagem com fundo retangular indesejado: preferir gerar novo asset correto, não remendar infinitamente com CSS.

---

## 9. Light/Dark — regra obrigatória

Toda página com imagens específicas por tema deve separar corretamente:

```txt
hero_light.png
hero_dark.png
card01_light.png
card01_dark.png
```

### 9.1 Light como padrão

```css
.page-hero::before {
    background-image: url("../../img/pagina/hero/hero_light.png");
}
```

### 9.2 Dark sobrescreve

```css
html.theme-dark .page-hero::before {
    background-image: url("../../img/pagina/hero/hero_dark.png");
}
```

### 9.3 Overlay também precisa ser separado

Nunca deixar overlay dark global afetando o light.

Errado:

```css
.page-hero::after {
    background: rgba(5, 16, 30, .88);
}
```

Correto:

```css
.page-hero::after {
    background: overlay claro;
}

html.theme-dark .page-hero::after {
    background: overlay escuro;
}
```

---

## 10. Cards — padrão visual

Os cards devem seguir o padrão do site:

- grid alinhado;
- imagem no topo;
- tag/eyebrow pequena;
- título claro;
- descrição curta;
- CTA na base;
- altura consistente;
- hover sutil;
- barra/acento inferior;
- sem cores hardcoded fora dos tokens;
- respeitar light/dark.

### 10.1 Estrutura base

```html
<article class="page-card">
    <figure class="page-card__media">
        <img src="..." alt="..." loading="lazy">
    </figure>

    <div class="page-card__body">
        <p class="page-card__tag">AUTOMAÇÃO</p>
        <h3 class="page-card__title">Título do card</h3>
        <p class="page-card__text">Descrição objetiva.</p>
        <a class="page-card__link" href="#">Saiba mais →</a>
    </div>
</article>
```

### 10.2 Comportamento

```txt
hover:
- leve subida
- sombra suave
- acento inferior mais visível
```

Não usar animações exageradas.

---

## 11. Imagens por página

Organização padrão:

```txt
static/img/home/
static/img/python/hero/
static/img/python/cards/
static/img/powerbi/
static/img/automacao/
static/img/excel/
static/img/curriculo/
static/img/contato/
```

### 11.1 Nomeação

```txt
hero_light.png
hero_dark.png

card01_light.png
card01_dark.png
card02_light.png
card02_dark.png
card03_light.png
card03_dark.png
card04_light.png
card04_dark.png
```

### 11.2 Atenção

Usar sempre:

```txt
light
```

Não usar:

```txt
ligth
```

---

## 12. Antes de alterar uma página

Checklist obrigatório:

```txt
1. Qual página é a referência visual?
2. O ajuste é de estrutura, texto, imagem, cards ou tema?
3. Quais arquivos podem ser alterados?
4. Quais arquivos estão protegidos?
5. A página precisa copiar a geometria da Home?
6. Existe light e dark?
7. O asset é banner, objeto isolado ou card?
8. Há risco de quebrar o tema oposto?
```

---

## 13. Prompt padrão para Codex — nova página

```txt
Você é um desenvolvedor front-end sênior. Criar/ajustar a página [NOME] do site ServicesBI.

Regra principal:
A Home é a fonte da verdade visual.
Antes de alterar, auditar:
- templates/pages/home.html
- static/css/pages/home.css

Não alterar a Home.

Arquivos permitidos:
- templates/pages/[pagina].html
- static/css/pages/[pagina].css

Não alterar:
- tokens.css
- base.css
- layout.css
- header.css
- footer.css
- JS
- outras páginas

Objetivo:
Replicar na página [NOME] a mesma geometria visual da Home:
- Hero com mesma altura;
- texto começando no mesmo eixo X e Y;
- mesma tipografia;
- mesmo espaçamento;
- mesmos botões;
- mesma lógica de cards;
- compatibilidade light/dark.

A única diferença é o conteúdo textual e a imagem específica da página.

Validação:
Rodar apenas:
python manage.py check

Não usar:
- Playwright
- Puppeteer
- Selenium
- Chrome headless

Retorno obrigatório:
1. arquivos alterados;
2. arquivos lidos como referência;
3. CSS final do Hero;
4. HTML final da section principal;
5. confirmação de que Home e globais não foram alterados.
```

---

## 14. Prompt padrão para Codex — ajuste de Hero

```txt
Corrigir apenas o Hero da página [NOME].

Problema:
[descrever problema]

Referência:
A Home está correta e deve ser usada como fonte da verdade.

Regra absoluta:
Não alterar:
- Home
- cards
- JS
- tokens.css
- base.css
- layout.css
- header.css
- footer.css
- outras seções

Arquivos permitidos:
- templates/pages/[pagina].html
- static/css/pages/[pagina].css

Tarefa:
1. Auditar o Hero da Home.
2. Identificar estrutura e valores reais de:
   - section
   - container
   - inner
   - content
   - eyebrow
   - title
   - lead
   - actions
   - bullets
   - visual
3. Aplicar o equivalente na página [NOME].
4. Não mover texto “no olho”.
5. Não criar padding manual diferente da Home.
6. Não alterar imagem salvo pedido explícito.

Validação:
python manage.py check

Retorno:
- arquivos alterados;
- classes da Home usadas como referência;
- CSS final;
- HTML final;
- confirmação de que arquivos protegidos não foram alterados.
```

---

## 15. Prompt padrão para Codex — ajuste de imagem do Hero

```txt
Corrigir apenas a imagem/arte visual do Hero da página [NOME].

Não alterar:
- texto
- posição do texto
- título
- botões
- bullets
- Home
- cards
- JS
- tokens globais

Diagnóstico:
Informar se o asset é:
1. objeto isolado;
2. imagem lateral;
3. banner completo;
4. imagem com fundo embutido.

Escolher a estratégia correta:

- objeto isolado: usar <img>;
- banner completo: usar background cover;
- arte lateral: usar background contain no lado direito;
- fundo embutido indesejado: recomendar novo asset.

Separar light/dark:
- light usa asset_light.png;
- dark usa asset_dark.png;
- overlay light não pode usar overlay dark;
- overlay dark só em html.theme-dark.

Validação:
python manage.py check

Retorno:
- estratégia escolhida;
- CSS final;
- confirmação de que texto e Home não foram alterados.
```

---

## 16. Erros que não podem se repetir

### 16.1 Não misturar estratégias

Não misturar ao mesmo tempo:

```txt
<img> lateral
background cover
background contain
mask agressiva
overlay global
```

Escolher uma arquitetura e limpar o resto.

### 16.2 Não corrigir dark quebrando light

Toda alteração em tema precisa ser testada nos dois temas.

### 16.3 Não mexer em container global

Não usar `max-width: none`, `padding-left` manual ou `transform` no container da página sem comparar com a Home.

### 16.4 Não tentar remover fundo embutido só com CSS indefinidamente

Se o asset tem fundo retangular gravado, a solução correta pode ser gerar outro asset.

---

## 17. Validação manual mínima

Depois de cada ajuste:

```txt
1. Abrir página em dark.
2. Abrir página em light.
3. Comparar com Home.
4. Conferir se texto começa no mesmo lugar.
5. Conferir se Hero tem altura compatível.
6. Conferir se cards não mudaram.
7. Conferir Console/F12 se necessário.
```

Não usar navegador headless.

---

## 18. Comandos leves permitidos

```powershell
python manage.py check
python manage.py runserver
git status --short
```

Se `python manage.py check` falhar com:

```txt
ModuleNotFoundError: No module named 'django'
```

provavelmente o venv não está ativo. Ativar o ambiente correto antes de validar.

---

## 19. Critério de pronto

Uma página só está pronta quando:

```txt
- Hero alinhado com a Home;
- tema light correto;
- tema dark correto;
- texto não pula entre páginas;
- imagem não invade texto;
- cards seguem o padrão;
- não houve alteração indevida em globais;
- não houve alteração indevida na Home;
- python manage.py check sem erros no venv.
```

---

## 20. Regra final

Se uma correção exigir mais de 2 tentativas, parar e fazer reset cirúrgico:

```txt
1. Identificar a arquitetura correta.
2. Remover remendos conflitantes.
3. Aplicar um único bloco limpo.
4. Validar light e dark.
```

Não continuar acumulando CSS.
