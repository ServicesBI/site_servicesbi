"""Central de comando do site — SÓ no PC do Leles.

Aparece quando o site roda pelo runserver em 127.0.0.1/localhost com DEBUG=True.
No site publicado (HTML estático) e no servidor (DEBUG=False) ela não existe:
as views respondem 404 e o template não é incluído.
"""
import io
import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.http import Http404, JsonResponse
from django.http.request import split_domain_port
from django.views.decorators.http import require_GET, require_POST

HOSTS_LOCAIS = {"127.0.0.1", "localhost", "::1", "[::1]"}
IPS_LOCAIS = {"127.0.0.1", "::1"}


def central_ativa(request):
    """True só no PC: DEBUG ligado, endereço local e acesso vindo da própria máquina.

    O export estático usa o host interno "testserver", então a central
    nunca entra na pasta cloudflare_dist.
    """
    if not settings.DEBUG:
        return False
    host, _porta = split_domain_port(request.get_host())
    return host in HOSTS_LOCAIS and request.META.get("REMOTE_ADDR", "") in IPS_LOCAIS


def _exigir_local(request):
    if not central_ativa(request):
        raise Http404()


def _git(*args):
    r = subprocess.run(
        ["git", *args], cwd=settings.BASE_DIR, capture_output=True,
        text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    return r.returncode, (r.stdout + r.stderr).rstrip()


@require_GET
def central_status(request):
    """Branch atual e arquivos alterados que ainda não foram commitados."""
    _exigir_local(request)
    _, branch = _git("branch", "--show-current")
    codigo, saida = _git("status", "--porcelain")
    if codigo != 0:
        return JsonResponse({"ok": False, "erro": saida})
    arquivos = [linha for linha in saida.splitlines() if linha.strip()]
    _, ultimo = _git("log", "-1", "--format=%h %s (%cr)")
    return JsonResponse({"ok": True, "branch": branch, "arquivos": arquivos, "ultimo_commit": ultimo})


@require_POST
def central_exportar(request):
    """Gera a pasta cloudflare_dist sem publicar nada."""
    _exigir_local(request)
    saida = io.StringIO()
    try:
        call_command("export_static_site", stdout=saida, stderr=saida)
    except Exception as erro:  # mostra o erro na central em vez de quebrar a página
        return JsonResponse({"ok": False, "erro": str(erro), "log": saida.getvalue()[-4000:]})
    return JsonResponse({"ok": True, "log": saida.getvalue()[-4000:]})


# ---------------------------------------------------------------------------
# Subir site — mesmo padrão do "Publicar online" do SIGE
# ---------------------------------------------------------------------------
PUBLICADOR = settings.BASE_DIR / "scripts" / "publicar_online.ps1"
LOG_DIR = settings.BASE_DIR / "scripts" / "logs"
STATUS_FILE = LOG_DIR / "status.json"
TEMPO_MAXIMO = timedelta(minutes=30)


def _processo_vivo(pid):
    """True se o processo existe (Windows). Na dúvida, considera vivo."""
    try:
        saida = subprocess.run(
            ["tasklist", "/FI", f"PID eq {int(pid)}", "/NH", "/FO", "CSV"],
            capture_output=True, text=True, timeout=10,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        ).stdout
    except (OSError, ValueError, subprocess.SubprocessError):
        return True
    return f'"{int(pid)}"' in saida


def _ler_status():
    try:
        dados = json.loads(STATUS_FILE.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return None
    dados["em_andamento"] = False
    try:
        dados["fim_legivel"] = datetime.fromisoformat(dados.get("fim", "")).strftime("%d/%m/%Y às %H:%M")
    except ValueError:
        dados["fim_legivel"] = dados.get("fim", "")
    if dados.get("estado") == "executando":
        try:
            inicio = datetime.fromisoformat(dados.get("inicio", ""))
            dados["em_andamento"] = datetime.now() - inicio < TEMPO_MAXIMO
        except ValueError:
            dados["em_andamento"] = False
        # janela do PowerShell fechada no meio: libera o botão na hora
        if dados["em_andamento"] and dados.get("pid") and not _processo_vivo(dados["pid"]):
            dados["em_andamento"] = False
    return dados


def _ler_log(status, linhas=80):
    if not status or not status.get("log"):
        return ""
    caminho = Path(status["log"])
    try:
        if caminho.resolve().parent != LOG_DIR.resolve():
            return ""
        texto = caminho.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""
    return "\n".join(texto.splitlines()[-linhas:])


@require_GET
def central_publicar_status(request):
    """Andamento da publicação (lido do status.json que o script grava)."""
    _exigir_local(request)
    status = _ler_status() or {}
    return JsonResponse({
        "estado": status.get("estado", ""),
        "mensagem": status.get("mensagem", ""),
        "fim_legivel": status.get("fim_legivel", ""),
        "em_andamento": status.get("em_andamento", False),
        "log": _ler_log(status),
    })


@require_POST
def central_publicar(request):
    """Abre a janela do PowerShell com scripts/publicar_online.ps1 (igual ao SIGE)."""
    _exigir_local(request)
    if os.name != "nt":
        return JsonResponse({"ok": False, "erro": "O botão Subir site só funciona no Windows (PowerShell)."})
    if not PUBLICADOR.exists():
        return JsonResponse({"ok": False, "erro": "Não encontrei scripts/publicar_online.ps1."})
    status = _ler_status()
    if status and status.get("em_andamento"):
        return JsonResponse({"ok": False, "erro": "Já existe uma publicação em andamento. Aguarde ela terminar."})

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    # mensagem opcional do commit (o script lê e apaga o arquivo)
    mensagem = " ".join((request.POST.get("mensagem") or "").split())[:200]
    arquivo_msg = LOG_DIR / "mensagem_commit.txt"
    if mensagem:
        arquivo_msg.write_text(mensagem, encoding="utf-8")
    elif arquivo_msg.exists():
        arquivo_msg.unlink()
    STATUS_FILE.write_text(json.dumps({
        "estado": "executando",
        "mensagem": "Abrindo o publicador",
        "inicio": datetime.now().isoformat(timespec="seconds"),
    }), encoding="utf-8")

    subprocess.Popen(
        ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(PUBLICADOR)],
        cwd=str(settings.BASE_DIR),
        creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0),
    )
    return JsonResponse({"ok": True})
