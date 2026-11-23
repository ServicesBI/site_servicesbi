# ServicesBI - Publicar site (servicesbi.com.br)
# Mesmo padrao do "Publicar online" do SIGE.
# Chamado pelo botao "Subir site" da Central de comando (clique no logo com o
# site rodando no PC), ou com duplo clique em scripts\PUBLICAR_SITE.cmd.
#
# Passos: confere pre-requisitos -> exporta o site (cloudflare_dist) ->
# commit no branch de trabalho -> envia ao GitHub (branch + main) ->
# git pull no servidor -> testa o site no ar.
# Nao faz checkout de branch: o runserver pode continuar ligado.
# Andamento gravado em scripts\logs\ (status.json + publicar_*.log), lido pela Central.

param([string]$Branch = "servicesbi-2.0")

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [Text.Encoding]::UTF8

$L    = Split-Path -Parent $PSScriptRoot
$K    = "$HOME\.ssh\servicesbi_oci"
$S    = "ubuntu@168.75.87.24"
$PastaServ = "/home/ubuntu/site_servicesbi"
$URLS = @("https://servicesbi.com.br/", "https://servicesbi.com.br/contato/")
$PY   = Join-Path $L ".venv\Scripts\python.exe"
if (-not (Test-Path $PY)) { $PY = "python" }
$TS   = Get-Date -Format "yyyyMMdd-HHmmss"
$INICIO = Get-Date -Format s

$SSHOPTS = @("-n", "-i", $K, "-o", "BatchMode=yes", "-o", "ConnectTimeout=15",
             "-o", "ServerAliveInterval=10", "-o", "ServerAliveCountMax=3")

$LogDir = Join-Path $PSScriptRoot "logs"
New-Item -ItemType Directory -Force $LogDir | Out-Null
$Log        = Join-Path $LogDir "publicar_$TS.log"
$Status     = Join-Path $LogDir "status.json"
$MsgArquivo = Join-Path $LogDir "mensagem_commit.txt"

$Host.UI.RawUI.WindowTitle = "ServicesBI - Publicar site"

function Log([string]$texto, [string]$cor = "Gray") {
    Write-Host $texto -ForegroundColor $cor
    Add-Content -Path $Log -Value $texto -Encoding UTF8
}

function Set-Status([string]$estado, [string]$mensagem) {
    [ordered]@{
        estado   = $estado
        mensagem = $mensagem
        inicio   = $INICIO
        fim      = (Get-Date -Format s)
        carimbo  = $TS
        pid      = $PID
        log      = $Log
    } | ConvertTo-Json | Set-Content -Path $Status -Encoding UTF8
}

# Roda um programa externo, mostra e grava a saida, e devolve o codigo de saida.
function Nativo([string]$exe, [string[]]$argumentos) {
    $anterior = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    & $exe @argumentos 2>&1 | ForEach-Object {
        $linha = if ($_ -is [System.Management.Automation.ErrorRecord]) { $_.Exception.Message } else { $_.ToString() }
        if ($linha -and $linha -ne "System.Management.Automation.RemoteException") { Log ("   " + $linha) }
    }
    $codigo = $LASTEXITCODE
    $ErrorActionPreference = $anterior
    return $codigo
}

function Passo([string]$texto) {
    Log ""
    Log $texto "Cyan"
    Set-Status "executando" $texto
}

$ok = $false
try {
    Log "ServicesBI - Publicar site  ($TS)" "White"
    Set-Status "executando" "Iniciando"
    Set-Location $L

    Passo "1/6 Conferindo pre-requisitos"
    if (-not (Test-Path $K)) { throw "Chave SSH nao encontrada em $K" }
    if ((Nativo "git" @("--version")) -ne 0) { throw "Git nao encontrado neste PC." }
    $atual = (& git branch --show-current).Trim()
    if ($atual -ne $Branch) { throw "Voce esta no branch '$atual'. Troque para '$Branch' antes de publicar." }
    # teste de conexao com limite total de 40s (nao pode ficar pendurado)
    $saidaTeste = Join-Path $env:TEMP "sbi_ssh_teste_$TS.txt"
    $argsTeste = ($SSHOPTS + @($S, "echo servidor-ok")) | ForEach-Object { if ($_ -match '\s') { '"' + $_ + '"' } else { $_ } }
    $p = Start-Process -FilePath "ssh" -ArgumentList $argsTeste `
         -NoNewWindow -PassThru -RedirectStandardOutput $saidaTeste -RedirectStandardError "$saidaTeste.err"
    $null = $p.Handle   # PS 5.1: sem isso o ExitCode volta vazio
    if (-not $p.WaitForExit(40000)) {
        try { $p.Kill() } catch {}
        throw "O servidor nao respondeu ao SSH em 40 segundos. Teste a conexao e tente de novo."
    }
    $p.WaitForExit()
    $textoTeste = (Get-Content $saidaTeste -Raw -ErrorAction SilentlyContinue) + ""
    Get-Content $saidaTeste, "$saidaTeste.err" -ErrorAction SilentlyContinue | ForEach-Object { if ($_) { Log ("   " + $_) } }
    Remove-Item $saidaTeste, "$saidaTeste.err" -ErrorAction SilentlyContinue
    if ($textoTeste -notmatch "servidor-ok") { throw "Nao consegui conectar no servidor por SSH (codigo $($p.ExitCode))" }

    Passo "2/6 Exportando o site (cloudflare_dist)"
    if ((Nativo $PY @("manage.py", "check")) -ne 0) { throw "manage.py check falhou no seu PC. Corrija antes de publicar." }
    if ((Nativo $PY @("manage.py", "export_static_site")) -ne 0) { throw "O export falhou (alguma pagina deu erro). Veja as linhas acima." }

    Passo "3/6 Salvando no Git (commit)"
    try {
        if ((Nativo "git" @("add", "-A")) -ne 0) { throw "git add falhou" }
        & git diff --cached --quiet
        if ($LASTEXITCODE -ne 0) {
            $msg = "Publicacao $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
            if (Test-Path $MsgArquivo) {
                $texto = ((Get-Content $MsgArquivo -Raw -Encoding UTF8) + "").Trim()
                if ($texto) { $msg = "$texto ($msg)" }
            }
            if ((Nativo "git" @("commit", "-m", $msg)) -ne 0) { throw "git commit falhou. Nada foi enviado." }
        } else {
            Log "   Nada novo para commitar."
        }
        Log ("   Commit: " + (& git log -1 --format="%h %s"))
    } finally {
        Remove-Item $MsgArquivo -ErrorAction SilentlyContinue
    }

    Passo "4/6 Enviando ao GitHub ($Branch e main)"
    if ((Nativo "git" @("fetch", "origin")) -ne 0) { throw "git fetch falhou" }
    if ((Nativo "git" @("push", "-u", "origin", "HEAD:refs/heads/$Branch")) -ne 0) { throw "git push do $Branch falhou" }
    & git merge-base --is-ancestor "origin/main" HEAD
    if ($LASTEXITCODE -ne 0) { throw "A main do GitHub tem commits que o $Branch nao tem. Nada foi publicado no site." }
    if ((Nativo "git" @("push", "origin", "HEAD:refs/heads/main")) -ne 0) { throw "git push da main falhou. Nada foi publicado no site." }
    # atualiza a main local sem trocar de branch (o runserver pode seguir ligado)
    $null = Nativo "git" @("fetch", ".", "HEAD:main")
    $commit = (& git rev-parse --short HEAD).Trim()
    Log "   GitHub atualizado ($Branch e main em $commit)." "Green"

    Passo "5/6 Atualizando o servidor"
    $cmd = "cd $PastaServ && git pull --ff-only origin main && git log --oneline -1"
    if ((Nativo "ssh" ($SSHOPTS + @($S, $cmd))) -ne 0) { throw "O git pull no servidor falhou. O site no ar nao mudou; veja as linhas acima." }

    Passo "6/6 Testando o site"
    Start-Sleep -Seconds 2
    $falhas = 0
    foreach ($u in $URLS) {
        try {
            $r = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 30 -Headers @{ "Cache-Control" = "no-cache" }
            Log ("   {0} -> HTTP {1}" -f $u, $r.StatusCode) "Green"
        } catch {
            $falhas++
            Log ("   {0} -> ERRO {1}" -f $u, $_.Exception.Message) "Red"
        }
    }
    if ($falhas -gt 0) { throw "O servidor foi atualizado, mas $falhas pagina(s) nao responderam. Confira o site." }

    $ok = $true
    Log ""
    Log "Publicado com sucesso (site e GitHub). No navegador, use Ctrl+F5 para nao pegar a versao antiga do cache." "Green"
    Set-Status "ok" "Publicado com sucesso (site e GitHub)"
}
catch {
    Log ""
    Log ("ERRO: " + $_.Exception.Message) "Red"
    Set-Status "erro" $_.Exception.Message
}

if ($ok) {
    Log "Esta janela fecha sozinha em 10 segundos."
    Start-Sleep -Seconds 10
} else {
    Read-Host "Pressione Enter para fechar"
    exit 1
}
