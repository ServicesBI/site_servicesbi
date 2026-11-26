# Botão "Subir" — como publicar uma aplicação direto do PC para a internet

> Guia do padrão usado no **SIGE** ("Publicar online") e no **site ServicesBI** ("Subir site", na Central de comando).
> Serve de receita para qualquer aplicação da ServicesBI, inclusive o **Jarvis**.
> Criado em 23/11/2026. Código de referência no site: `apps/pages/central.py`, `templates/includes/central_comando.html`, `scripts/publicar_online.ps1`.

---

## 1. A ideia em uma frase

Um botão que **só existe no PC do desenvolvedor** abre uma **janela do PowerShell** que roda um **script de publicação em passos numerados**; o script grava o andamento num **status.json**, e a tela da aplicação lê esse arquivo a cada 3 segundos para mostrar o progresso.

```
[Botão na tela]  --POST-->  [Backend local]  --abre-->  [Janela PowerShell: publicar_online.ps1]
      ^                                                        |
      |                                                        v
      +---- GET status a cada 3 s ----  scripts/logs/status.json + publicar_*.log
```

## 2. As 4 peças

| Peça | No site ServicesBI | Função |
|---|---|---|
| **Trava "só no meu PC"** | `central_ativa()` em `apps/pages/central.py` | Botão e rotas só existem no PC; fora dele respondem 404 |
| **Backend (3 rotas)** | `central/publicar/`, `central/publicar/status/` (+ `central/status/`) | Inicia a janela e devolve o andamento |
| **Script de publicação** | `scripts/publicar_online.ps1` (+ `PUBLICAR_SITE.cmd`) | Faz o trabalho em passos, grava status e log |
| **Tela** | `templates/includes/central_comando.html` | Campo de descrição, confirmação, botão e andamento |

## 3. Passo a passo para montar

### Passo 1 — Trava "só no meu PC"

O botão nunca pode aparecer na versão publicada nem responder a quem vem de fora. No site são 3 condições juntas:

```python
def central_ativa(request):
    if not settings.DEBUG:                       # servidor roda com DEBUG=False
        return False
    host, _porta = split_domain_port(request.get_host())
    return host in {"127.0.0.1", "localhost", "::1", "[::1]"} \
        and request.META.get("REMOTE_ADDR", "") in {"127.0.0.1", "::1"}
```

Toda rota da publicação começa chamando isso; se for falso, `raise Http404()`.
No SIGE a trava ainda exige `SIGE_PUBLICAR_ONLINE=True` no `.env` local, usuário superusuário e Windows.
**Jarvis:** como ele já roda só no PC, a trava mínima é aceitar apenas pedidos de `127.0.0.1`/`::1` (e, de preferência, uma variável no `.env`, ex. `JARVIS_PUBLICAR=True`).

### Passo 2 — Rota que inicia a publicação (POST)

1. Recusa se já houver publicação em andamento (lê o status.json, Passo 5).
2. Grava a descrição do commit (opcional) em `scripts/logs/mensagem_commit.txt` — o script lê e apaga.
3. Grava um status inicial `{"estado":"executando","mensagem":"Abrindo o publicador","inicio":"<agora>"}`.
4. Abre a janela nova do PowerShell **sem esperar ela terminar**:

```python
subprocess.Popen(
    ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(SCRIPT)],
    cwd=str(BASE_DIR),
    creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0),
)
```

`CREATE_NEW_CONSOLE` é o que faz aparecer a janela própria. Responde `{"ok": true}` na hora.
A rota é POST e protegida pelo CSRF do Django (o JS manda o cabeçalho `X-CSRFToken`).

### Passo 3 — O script de publicação (`publicar_online.ps1`)

Estrutura que se repete em todos os projetos:

```powershell
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "ServicesBI - Publicar site"
# pasta de logs, arquivo de log com data/hora, status.json

function Log($texto, $cor = "Gray")      { Write-Host ...; Add-Content $Log ... }   # tela + arquivo
function Set-Status($estado, $mensagem)  { ... | ConvertTo-Json | Set-Content $Status }  # estado, mensagem, inicio, fim, pid, log
function Nativo($exe, $argumentos)       { ... }   # roda git/ssh/python, mostra e grava a saída, devolve o código
function Passo($texto)                   { Log $texto "Cyan"; Set-Status "executando" $texto }

try {
    Passo "1/6 Conferindo pre-requisitos"   # chave SSH, branch certo, teste de SSH com limite de 40 s
    Passo "2/6 Exportando o site"           # manage.py check + export_static_site
    Passo "3/6 Salvando no Git (commit)"    # git add -A; commit com a descrição + data
    Passo "4/6 Enviando ao GitHub"          # push do branch e da main (sem trocar de branch)
    Passo "5/6 Atualizando o servidor"      # ssh ... git pull --ff-only
    Passo "6/6 Testando o site"             # Invoke-WebRequest nas URLs principais
    Set-Status "ok" "Publicado com sucesso"
} catch {
    Log ("ERRO: " + $_.Exception.Message) "Red"
    Set-Status "erro" $_.Exception.Message
}
# sucesso: fecha sozinha em 10 s · erro: "Pressione Enter para fechar"
```

Regras que aprendemos:
- **Cada passo para no primeiro erro** (`throw`) e diz o motivo em português simples. Nada de seguir "meio quebrado".
- **Teste de SSH antes de tudo**, com limite de 40 s. Se o servidor não responde, para no passo 1, antes de commitar ou enviar qualquer coisa (foi o que aconteceu em 23/11 com o servidor travado).
- **SSH sem pergunta**: `-n -o BatchMode=yes -o ConnectTimeout=15 -o ServerAliveInterval=10 -o ServerAliveCountMax=3`, com a chave `~\.ssh\servicesbi_oci`.
- **Não trocar de branch** com a aplicação rodando: a `main` é atualizada com `git push origin HEAD:refs/heads/main` (e `git fetch . HEAD:main` para a main local). Antes confere com `git merge-base --is-ancestor origin/main HEAD` que é só avanço.
- **Texto do script sem acentos** (o PowerShell 5.1 lê o arquivo sem BOM como ANSI).
- **Logs fora do git**: `scripts/logs/` no `.gitignore`, senão o próprio log entra no commit.
- Um `.cmd` ao lado (`PUBLICAR_SITE.cmd`) roda o mesmo script com duplo clique, sem precisar da tela.

### Passo 4 — O que muda de projeto para projeto: o "como chega no servidor"

| Projeto | Como a versão nova chega ao servidor |
|---|---|
| **Site** (HTML estático) | Exporta para `cloudflare_dist/` → commit → push → no servidor `git pull`. O Nginx lê a pasta direto, nada a reiniciar |
| **SIGE** (Django rodando no servidor) | `check` + migrations conferidas → commit → empacota (`empacotar.py`, sem .env/venv/media) → `scp` do pacote → script remoto faz backup do código e do banco, migra, `collectstatic`, reinicia, e **restaura sozinho se falhar** → testa as URLs → push no GitHub |
| **Jarvis** | Decidir (ver seção 5) |

### Passo 5 — Rota de status (GET) e "janela fechada no meio"

Lê `status.json` e devolve `estado`, `mensagem`, `fim_legivel`, `em_andamento` e as últimas 80 linhas do log.
`em_andamento` só é verdadeiro se: estado = `executando` **e** começou há menos de 30 min **e** o processo da janela (`pid`) ainda existe (`tasklist /FI "PID eq <pid>"`). Assim, se alguém fechar a janela no meio, o botão é liberado na hora.
Segurança: só lê log que esteja **dentro** de `scripts/logs/`.

### Passo 6 — A tela

1. Campo "Descrição do commit (opcional)" e botão **Subir**.
2. `confirm("Publicar agora no servicesbi.com.br? ...")` antes de enviar.
3. POST → "Publicação iniciada. Uma janela do PowerShell abriu com o andamento."
4. A cada 3 s busca o status: mostra "Publicando… 4/6 Enviando ao GitHub" e o log; trava o botão enquanto `em_andamento`.
5. No fim: "Última publicação: concluída em 23/11/2026 às 12:15" (ou o erro).

### Passo 7 — Testar

1. Aplicação rodando no PC → botão aparece. Acesso de fora / versão publicada → botão some e as rotas dão 404.
2. Publicação com sucesso → janela fecha em 10 s, tela mostra "concluída".
3. Forçar erro (ex.: desligar a internet) → para no passo 1, janela espera Enter, tela mostra o erro, **nada foi commitado ou enviado**.
4. Fechar a janela no meio → o botão volta a ficar liberado.

## 4. Problemas que já tivemos (e a solução)

| Sintoma | Causa | Solução |
|---|---|---|
| "Connection timed out during banner exchange" no passo 1 | Servidor Oracle travado/sem memória | Esperar ou reiniciar a VM no painel da Oracle; o script já protege, nada é enviado |
| Script recusava rodar ("tem algo na porta 8000") | Checagem antiga do `publicar_site.ps1` | O publicador novo não troca de branch, então pode rodar com a aplicação ligada |
| Publicou, mas o navegador mostra a versão antiga | Servidor manda guardar CSS/JS por 30 dias | Pendente: colocar `?v=<versão>` nos endereços dos arquivos a cada publicação |
| SIGE sem ícone/estilo novo depois de publicar | `DEBUG=False` usa `staticfiles` | `collectstatic` + reiniciar (no SIGE o script remoto já faz) |

## 5. Para o Jarvis: o que decidir antes de montar

1. **"Subir" o quê e para onde?**
   - **Só o código para o GitHub** (backup/versão): o script faz `check` → commit → push. É o caso mais simples.
   - **Uma parte web na internet** (ex.: página ou painel em `servicesbi.com.br/jarvis-app/`): segue o modelo do **SIGE** (pacote + script remoto com backup e restauração).
   - **Novo instalador para outros PCs**: o script gera o build/instalador e envia para um lugar de download.
2. **Onde fica o botão:** no HUD 3.0 (ex.: dentro do Zeus ou de uma tela "Sistema"), seguindo a trava do Passo 1.
3. **Checagens do passo 2 do Jarvis:** testes que rodam antes de publicar (servidor responde, banco conecta, nenhum segredo em arquivo que vai para o git).
4. **Cuidados específicos do Jarvis:** há 171 arquivos sem commit desde 12/11 — revisar esse diff **antes** do primeiro "Subir", porque o `git add -A` leva tudo. Conferir que `.env`, chaves de API, tokens OAuth do Google e logs estão no `.gitignore`. As rotas `/api/automation/*` sem autenticação **não** podem ir para a internet como estão.

## 6. Prompt pronto para passar ao Claude do projeto Jarvis

> Quero um botão "Subir" no Jarvis no mesmo padrão do SIGE e do site ServicesBI. Leia o guia `D:\python\site_servicesbi\docs\BOTAO_SUBIR.md` e, como referência de código, `D:\python\site_servicesbi\apps\pages\central.py`, `templates\includes\central_comando.html` e `scripts\publicar_online.ps1` (e no SIGE `apps\administracao\publicacao.py` e `deploy\publicar_online.ps1`). Antes de programar, me mostre um esboço: o que o botão vai publicar, para onde, os passos numerados do script e onde o botão fica no HUD. Não faça commit nem publique nada sem eu pedir. Antes do primeiro uso, revise comigo os arquivos não commitados e o `.gitignore`.
