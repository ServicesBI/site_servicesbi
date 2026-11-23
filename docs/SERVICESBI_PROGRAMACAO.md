# ServicesBI — Guia de Programação do Site (v2026)

> **Fonte de verdade técnica do site servicesbi.com.br.** Reúne como o código está organizado, como rodar, exportar e publicar, e as decisões técnicas tomadas nas conversas com o Claude (nov/2026).
> Visual (cores, fontes, componentes, decisões de design): `docs/SERVICESBI_IDENTIDADE_VISUAL.md`.
> Publicação passo a passo: `docs/PUBLICAR_SITE.md`.
> **Última atualização: 23/11/2026.**

---

## 1. Visão geral

- **Empresa:** ServicesBI — consultoria financeira respaldada por análise de dados, BI e automação. Responsável: **Leles Júnior** (Gestão Financeira + Análise de Dados).
- **Objetivo do site:** gerar contatos de clientes de consultoria (e, em segundo plano, recrutadores, pelo "Sobre").
- **Projeto:** "ServicesBI 2.0", reestruturação feita a partir de 18/11/2026, seguindo o plano `plano_de_reestrutura_o_servicesbi.md` (no projeto do Claude; cópia em `Claude outputs/plano_reestruturacao_servicesbi_v2.md`).
- **Como funciona:** o site é feito em **Django**, mas vai para o ar como **HTML estático**. O comando `export_static_site` gera a pasta `cloudflare_dist/`, e o Nginx do servidor serve essa pasta.

## 2. Stack e ambiente

| Item | Valor |
|---|---|
| Linguagem / framework | Python + Django |
| Front | HTML (templates Django), CSS modular com tokens, JavaScript puro |
| Fontes | Inter + IBM Plex Mono (Google Fonts) |
| Pasta local | `D:\python\site_servicesbi` (aberta no VS Code) |
| Repositório | GitHub `ServicesBI/site_servicesbi` |
| Branch de trabalho | `servicesbi-2.0` · produção: `main` · backup do site antigo: `backup/site-v1` |
| Settings em uso | `core.settings` (definido no `manage.py`) |
| Banco | SQLite por padrão (`DB_ENGINE` no `.env` permite PostgreSQL); o site público não depende de banco |
| `.env` | Lido por `python-dotenv`; está no `.gitignore` (não vai para o GitHub) |
| Variáveis úteis no `.env` | `DEBUG`, `SITE_URL`, `CLARITY_ID` (Microsoft Clarity), `DB_ENGINE` e dados do banco |

Rodar localmente (com o ambiente virtual ativo):

```powershell
python manage.py runserver
# abrir http://127.0.0.1:8000/  (Ctrl+F5 para não ver versão antiga em cache)
```

## 3. Estrutura de pastas

```txt
site_servicesbi/
├── apps/
│   ├── pages/                 # app do site público
│   │   ├── views.py           # dados e views de todas as páginas
│   │   ├── urls.py            # rotas
│   │   ├── context_processors.py  # variáveis globais (WhatsApp, e-mail, LinkedIn, Clarity)
│   │   └── management/commands/export_static_site.py
│   └── sige/                  # só a entrada /sige/ → tela de login (o SIGE de verdade é outro projeto)
├── core/                      # settings e urls EM USO
├── config/                    # settings antigos (duplicidade, não usado) — limpeza pendente
├── sitepages/                 # app antigo vazio — limpeza pendente
├── templates/
│   ├── base.html              # cabeçalho comum: SEO, Open Graph, favicon, Clarity, fontes, CSS, tema
│   ├── includes/              # header, footer, menu_links, logo_mark, theme_toggle, ferramentas_cards
│   ├── pages/                 # uma página por arquivo (+ pasta antigas/ com backups)
│   ├── sige/login.html        # login do SIGE dentro do site
│   ├── robots.txt, sitemap.xml
├── static/
│   ├── css/                   # tokens.css, base, layout, buttons, cards, header, footer, v2.css, whatsapp-float.css
│   │   └── pages/             # CSS por página (home-v3.css é o da home atual)
│   ├── js/                    # theme-init.js, theme.js, contato.js, home-*.js
│   └── img/                   # brand/ (logos e favicons), home/, powerbi/, sobre/ ... (WebP)
├── cloudflare_dist/           # SAÍDA do export (o que vai para o ar) — não editar à mão
├── scripts/publicar_site.ps1  # rotina de publicação
├── docs/                      # documentação (este arquivo, identidade visual, publicação)
└── Claude outputs/            # arquivos gerados pelo Claude (prévias, backups, planos) — não vai para o site
```

## 4. Páginas e rotas

Rotas em `apps/pages/urls.py`; views em `apps/pages/views.py`.

| URL | Template | Observação |
|---|---|---|
| `/` | `pages/home.html` | Home = Consultoria Financeira (Modelo B ajustado). CSS `pages/home-v3.css` |
| `/consultoria-financeira/` | view `consultoria_page` | O menu "Consultoria Financeira" aponta para a home |
| `/power-bi/` | `pages/powerbi.html` | "BI & Dashboards" |
| `/produtos/` | `pages/produtos.html` | "Nossos Produtos": SIGE, Jarvis, Automações n8n, Excel corporativo |
| `/cases/` | `pages/cases.html` | |
| `/sobre/` | `pages/sobre.html` | Inclui acesso ao currículo |
| `/contato/` | `pages/contato.html` | Formulário → WhatsApp |
| `/automacoes/`, `/python/`, `/excel/` | páginas internas | Termos técnicos ficam aqui, não na home |
| `/sige-servicesbi/` | `pages/sige_institucional.html` | Página institucional do SIGE |
| `/jarvis/` | `pages/jarvis.html` | Jarvis em desenvolvimento, lista de espera |
| `/curriculo/` | `pages/curriculo.html` | Link secundário |
| `/robots.txt`, `/sitemap.xml` | templates | Gerados a partir de `PAGINAS_PUBLICAS` |
| `/sige/` → `/sige/login/` | `sige/login.html` | App `apps.sige` (só login/logout) |
| `/admin/` | Django admin | Servido pelo gunicorn no servidor |

**Página nova — tem que entrar em 3 lugares:**
1. `apps/pages/urls.py` (rota);
2. `PAGINAS_PUBLICAS` em `apps/pages/views.py` (sitemap);
3. `PAGES` em `apps/pages/management/commands/export_static_site.py` (export).

Menu e rodapé usam a mesma lista: `templates/includes/menu_links.html`.

## 5. Conteúdo editável sem mexer em HTML (`apps/pages/views.py`)

| Constante | Para que serve |
|---|---|
| `NOVIDADES` | Seção "Novidades" da home. **Vazia = seção escondida.** Formato: `{"data": "11/2026", "ferramenta": "SIGE", "texto": "..."}`, mais recentes primeiro |
| `DRE_ILUSTRATIVA`, `CAIXA_SEMANAS`, `CAIXA_MINIMO` | Painel do topo da home (dados ilustrativos) |
| `FOTO_SOBRE` | `img/sobre/leles.webp` — se o arquivo existir, a foto aparece sozinha; senão mostra "LJ" |
| `SIGE_DEMO_URL` | `https://servicesbi.com.br/sige-demo/login/` (demo aberta ao público) |
| `FERRAMENTAS_HOME`, `PRODUTOS_DETALHE`, `ANCORAS_PRODUTOS` | Cards de ferramentas/produtos |
| `CASES_HOME`, `PASTAS_POWERBI`, `METAS_*`, `HERO_CARDS_*` | Cases, dashboards e cards dos heróis das páginas |

## 6. Contato, WhatsApp e medição

- **Variáveis globais** (`apps/pages/context_processors.py`), disponíveis em todo template: `WHATSAPP_NUMERO`, `WA_GERAL`, `WA_DIAGNOSTICO`, `WA_PLANILHA`, `WA_JARVIS`, `EMAIL_CONTATO`, `LINKEDIN_URL`, `SITE_URL`, `CLARITY_ID`.
- **Formulário de contato** (`static/js/contato.js`): monta a mensagem com os campos e **abre o WhatsApp** (`wa.me`). Não depende de servidor nem de webhook. Tem honeypot anti-spam. Para trocar por n8n ou Formspree no futuro, basta substituir a função que abre o WhatsApp por um `fetch()`.
- **Botão flutuante do WhatsApp** em todas as páginas (`base.html` + `whatsapp-float.css`).
- **Microsoft Clarity:** só carrega se `CLARITY_ID` estiver preenchido no `.env`.
- **Número de WhatsApp no código:** `5561993029988` (em `context_processors.py` e `contato.js`). ⚠ O número informado como canal da ServicesBI é **(61) 98574-9988** — conferir qual é o correto antes de divulgar.
- E-mail atual: `servicesbi.ltda@gmail.com` (plano: `contato@servicesbi.com.br` via Cloudflare Email Routing).

## 7. Tema claro/escuro

- `static/js/theme-init.js` roda no `<head>` antes do CSS: aplica a classe `theme-dark` no `<html>` (o site **abre no escuro**) ou o tema salvo no `localStorage`.
- `static/js/theme.js` cuida do botão ☀/☾ (`templates/includes/theme_toggle.html`).
- Cores só por tokens em `static/css/tokens.css` (`:root` = claro, `html.theme-dark` = escuro). Detalhes em `SERVICESBI_IDENTIDADE_VISUAL.md`.
- `<meta name="theme-color" content="#0A1217">` em `base.html` (barra do navegador no celular).

## 8. SEO e compartilhamento (`templates/base.html`)

Cada página define os blocos `title`, `meta_description` e `og_title`. O `base.html` já inclui: Open Graph e Twitter Card (`og-servicesbi.png` 1200×630), `canonical`, favicons, dados estruturados (JSON-LD na home), `robots.txt` e `sitemap.xml`.

## 9. Exportar e publicar

Resumo (detalhes em `docs/PUBLICAR_SITE.md`):

```powershell
# no terminal do VS Code, em D:\python\site_servicesbi, com o runserver parado
.\scripts\publicar_site.ps1 -Mensagem "O que mudou nesta atualização"
```

O jeito principal agora é o botão **Subir site** da Central de comando (seção 13). Pelo terminal continua valendo o script antigo. O script: exporta (`python manage.py export_static_site` → `cloudflare_dist/`) → commit e push do `servicesbi-2.0` → pergunta "Publicar agora? (s/n)" → junta na `main` e envia → entra no servidor por SSH e faz `git pull` → confere o site no ar. Opções: `-SemExportar`, `-Sim`, `-Branch`.

**Servidor:** Oracle Cloud (OCI), Ubuntu, `servicesbi-vm`. Nginx serve `/` e `/static/` direto de `/home/ubuntu/site_servicesbi/cloudflare_dist` (não precisa reiniciar). `/sige/` e `/sige-demo/` vão para o Django do SIGE (outro projeto, `/home/ubuntu/SIGE_ServicesBI`). `/admin/` vai para o gunicorn do site. DNS na Cloudflare, sem proxy. **O GitHub não publica sozinho**: o site só muda quando o servidor faz `git pull`.

Depois de publicar: abrir o site com **Ctrl+F5**.

## 10. Projetos ligados ao site

| Projeto | Onde | Relação com o site |
|---|---|---|
| **SIGE** (ERP) | `D:\python\SIGE_ServicesBI` · no ar em `/sige/` e demo em `/sige-demo/` | "Extensão" do site: mesma identidade visual. Projeto Claude separado. Roda com `DEBUG=False`: depois de mudar estáticos, rodar `python manage.py collectstatic --noinput`, reiniciar e Ctrl+F5 (no instalador/executável, gerar o build de novo) |
| **Jarvis** | projeto próprio | Página `/jarvis/` com lista de espera pelo WhatsApp; favicon da ServicesBI no `public/index.html` |
| **Compras** | projeto próprio | Favicon da ServicesBI no `base.html` e no login |

Regra para qualquer sistema novo: favicon da ServicesBI (3 linhas, ver identidade visual, seção 2) e mesma paleta.

## 11. Regras de trabalho com o Claude / Codex

- **Não quebrar o que funciona.** Mudanças pequenas e testadas; nada de refatorar sem pedido.
- **Mudança grande → esboço primeiro**, aprovação do Leles, depois código.
- **Commit, push e publicação só quando o Leles pedir.** O Leles publica pedindo ao Claude Code no VS Code (prompt pronto), não roda scripts sozinho.
- Antes de mexer: `git status` para ver alterações dele ainda não commitadas — não sobrescrever.
- Testar nos temas claro e escuro, desktop e celular (390 px). Rodar `python manage.py export_static_site` sem erro.
- Arquivos de apoio (prévias, backups, zips) vão para `Claude outputs/`, nunca para `static/` ou `templates/`.
- Não editar `cloudflare_dist/` à mão: ela é sempre regerada pelo export.

## 12. Histórico de commits importantes (branch `servicesbi-2.0`)

| Commit | O que fez |
|---|---|
| `3305520` | Etapa 1: destravar contatos (formulário → WhatsApp, botão flutuante, CTA do hero) |
| `7be4e44` | Imagens convertidas para WebP |
| `97cfeaf` | Etapas 2 a 4: SEO, nova home, menu e novas páginas |
| `3463162` | Favicon com o logo oficial |
| `668a520` | Identidade visual 2026: paleta do tema claro e manual da marca |
| `db1f15e` | Tema dark premium (preto, violeta e bege) — **substituído** pela paleta do SIGE em 22/11 |
| `34669c4` | Nova home aprovada (Modelo B ajustado) |
| `a934cef` | Home sem a grade quadriculada no fundo do topo |
| `6b6b239` | Menu "Nossos Produtos", rodapé com redes, seção "Quem conduz", páginas Produtos e Cases |
| `2a7a79e` | Script e guia de publicação |

**Alterações locais ainda sem commit (em 23/11/2026):** tema dark com a paleta do SIGE (`tokens.css`, `v2.css`, `pages/home-v3.css`, `theme-color` no `base.html`) e ajustes em `templates/sige/login.html` (capa do SIGE com a identidade do site 2.0 + favicon).

## 13. Central de comando (só no seu PC)

Janelinha no estilo da central do SIGE, para subir o site sem usar o terminal. Criada em 23/11/2026.

- **Como abrir:** com o site rodando pelo `runserver` no PC (`http://127.0.0.1:8000`), clique no **logo**. No site publicado o logo continua levando à página inicial.
- **Por que não vai para o ar:** a central só aparece com `DEBUG=True` **e** endereço local (127.0.0.1/localhost) **e** acesso vindo da própria máquina. O export usa o host interno `testserver`, então ela nunca entra na `cloudflare_dist`. No servidor (`DEBUG=False`) as rotas `/central/...` respondem 404.
- **O que tem:**
  - **Subir site** (mesmo padrão do "Publicar online" do SIGE): descrição do commit opcional → confirmação → abre a janela **"ServicesBI - Publicar site"** do PowerShell com `scripts\publicar_online.ps1`, em 6 passos: 1 pré-requisitos (chave SSH, branch `servicesbi-2.0`, teste de SSH em até 40 s) · 2 `check` + export · 3 commit · 4 push do `servicesbi-2.0` e da `main` no GitHub (sem trocar de branch, então o `runserver` pode ficar ligado) · 5 `git pull` no servidor · 6 teste do site no ar. Sucesso: a janela fecha sozinha em 10 s. Erro: mostra o motivo e espera Enter. A central mostra o andamento (lê `scripts\logs\status.json` e o log, a cada 3 s) e bloqueia um segundo clique enquanto houver publicação. Também dá para rodar com duplo clique em `scripts\PUBLICAR_SITE.cmd`. Os logs ficam em `scripts\logs\` (fora do git).
  - **Só exportar:** roda `export_static_site` e mostra o resultado.
  - **Ver o que mudou:** branch, arquivos alterados sem commit e último commit.
  - **Atalhos:** Página inicial, Administração do site (`/admin/`), Site no ar, SIGE, SIGE demo, GitHub do site.
- **Arquivos:** `apps/pages/central.py` (views e a regra `central_ativa`), `scripts/publicar_online.ps1`, rotas `central/status/`, `central/exportar/`, `central/publicar/`, `central/publicar/status/` em `apps/pages/urls.py`, flag `CENTRAL_LOCAL` em `context_processors.py`, e `templates/includes/central_comando.html` (HTML, CSS e JS juntos, para nada ir para `static/`), incluído no `header.html`.
- **Para acrescentar um botão/atalho:** editar `central_comando.html` (links) ou criar uma view nova em `central.py` sempre começando com `_exigir_local(request)`.
- **Ainda não tem:** subir SIGE e Jarvis (outros projetos; precisam da pasta `D:\python\SIGE_ServicesBI` conectada e da rotina de publicação de cada um).

## 14. Pendências técnicas

- [ ] Commitar e publicar o dark novo (quando o Leles pedir).
- [ ] Confirmar o número de WhatsApp correto (seção 6).
- [ ] `CLARITY_ID` no `.env` do servidor/export e cadastro no Google Search Console; Google Business Profile.
- [ ] E-mail `contato@servicesbi.com.br`.
- [ ] Planilha gratuita de fluxo de caixa (12 semanas) precisa existir — a home oferece pelo WhatsApp.
- [ ] Limpeza (baixa prioridade): remover `sitepages/` e a duplicidade `config/` × `core/`.
- [ ] Teste no PageSpeed Insights (meta > 80 no celular).
- [ ] Decisões de negócio em aberto: nicho/região, pacotes e se os valores aparecem.
