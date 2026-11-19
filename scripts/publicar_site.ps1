<#
  Publicar o site ServicesBI (servicesbi.com.br)

  Faz tudo em sequência e para no primeiro erro:
    1. Exporta o site Django para cloudflare_dist/ (export_static_site)
    2. Commit e push do branch de trabalho (padrão: servicesbi-2.0)
    3. Atualiza a main (merge --ff-only) e envia para o GitHub
    4. Entra no servidor OCI e faz git pull (o Nginx lê cloudflare_dist direto)
    5. Confere se o site no ar foi atualizado

  Uso (no terminal do VS Code, na pasta do projeto, com o runserver PARADO):
    .\scripts\publicar_site.ps1 -Mensagem "Ajusta página Nossos Produtos"

  Opções:
    -Mensagem "texto"   mensagem do commit (obrigatória se houver alterações)
    -SemExportar        pula o export (use se já exportou)
    -Branch nome        branch de trabalho (padrão: servicesbi-2.0)
    -Sim                não pede confirmação antes de publicar
#>
param(
    [string]$Mensagem = "",
    [string]$Branch = "servicesbi-2.0",
    [switch]$SemExportar,
    [switch]$Sim
)

# ---- Configuração do servidor ----
$ServidorUser = "ubuntu"
$ServidorIP   = "168.75.87.24"
$ChaveSSH     = Join-Path $HOME ".ssh\servicesbi_oci"
$PastaServ    = "/home/ubuntu/site_servicesbi"
$SiteURL      = "https://servicesbi.com.br"

$ErrorActionPreference = "Stop"

function Passo($texto) { Write-Host "`n=== $texto ===" -ForegroundColor Cyan }
function Falha($texto) { Write-Host "`nERRO: $texto" -ForegroundColor Red; exit 1 }
function Checar($texto) { if ($LASTEXITCODE -ne 0) { Falha $texto } }

# Garante que está na raiz do projeto
$Raiz = Split-Path -Parent $PSScriptRoot
Set-Location $Raiz
if (-not (Test-Path "manage.py")) { Falha "Rode o script de dentro do projeto site_servicesbi." }

# Confere branch atual
$atual = (git branch --show-current).Trim()
if ($atual -ne $Branch) { Falha "Você está no branch '$atual'. Troque para '$Branch' antes (git checkout $Branch)." }

# Avisa se o runserver parece estar rodando
$porta = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue
if ($porta) { Falha "Tem algo rodando na porta 8000 (runserver?). Pare com Ctrl+C e rode de novo." }

# 1. Export
if (-not $SemExportar) {
    Passo "1/5 Exportando o site para cloudflare_dist"
    $py = ".\.venv\Scripts\python.exe"
    if (-not (Test-Path $py)) { $py = "python" }
    & $py manage.py export_static_site
    Checar "O export falhou. Veja a mensagem acima (alguma página deu erro)."
} else {
    Passo "1/5 Export pulado (-SemExportar)"
}

# 2. Commit + push do branch
Passo "2/5 Commit e push do branch $Branch"
git add -A
$pendentes = git status --porcelain
if ($pendentes) {
    if (-not $Mensagem) { Falha "Há alterações para commitar. Rode de novo com -Mensagem `"o que mudou`"." }
    git commit -m $Mensagem
    Checar "O commit falhou."
} else {
    Write-Host "Nada novo para commitar."
}
git push -u origin $Branch
Checar "O push do branch $Branch falhou."

# Confirmação antes de mexer no site no ar
if (-not $Sim) {
    Write-Host "`nPróximo passo: publicar na main e atualizar $SiteURL." -ForegroundColor Yellow
    $resp = Read-Host "Publicar agora? (s/n)"
    if ($resp -notin @("s", "S", "sim", "Sim")) { Write-Host "Parado. Nada foi publicado no site."; exit 0 }
}

# 3. Main
Passo "3/5 Atualizando a main"
git checkout main
Checar "Não consegui trocar para a main."
git pull --ff-only origin main
if ($LASTEXITCODE -ne 0) { git checkout $Branch; Falha "A main local não bate com o GitHub. Nada foi publicado." }
git merge --ff-only $Branch
if ($LASTEXITCODE -ne 0) { git checkout $Branch; Falha "A main tem commits que o $Branch não tem (merge não é fast-forward). Nada foi publicado." }
git push origin main
$okPush = $LASTEXITCODE
git checkout $Branch
if ($okPush -ne 0) { Falha "O push da main falhou." }
$commit = (git rev-parse --short HEAD).Trim()

# 4. Servidor
Passo "4/5 Atualizando o servidor ($ServidorIP)"
if (-not (Test-Path $ChaveSSH)) { Falha "Chave SSH não encontrada em $ChaveSSH." }
$remoto = "cd $PastaServ && git pull --ff-only origin main && git log --oneline -1"
ssh -i $ChaveSSH -o ConnectTimeout=20 "$ServidorUser@$ServidorIP" $remoto
Checar "O git pull no servidor falhou. Entre com: ssh -i `"$ChaveSSH`" $ServidorUser@$ServidorIP"

# 5. Conferência
Passo "5/5 Conferindo o site no ar"
curl.exe -sI $SiteURL | Select-String "HTTP/|Last-Modified"
Write-Host "`nPronto! Commit $commit publicado em $SiteURL" -ForegroundColor Green
Write-Host "Dica: abra o site com Ctrl+F5 para não ver a versão em cache."
