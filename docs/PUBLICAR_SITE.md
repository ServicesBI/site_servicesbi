# Como publicar o site ServicesBI

## Jeito rápido (script)

No terminal do VS Code, na pasta `D:\python\site_servicesbi`, com o `runserver` **parado** (Ctrl+C):

```powershell
.\scripts\publicar_site.ps1 -Mensagem "O que mudou nesta atualização"
```

O script exporta o site, faz commit e push do `servicesbi-2.0`, pede confirmação, atualiza a `main`, entra no servidor, faz `git pull` e confere se o site no ar mudou. Se algo der errado, ele para e diz onde parou.

Opções:
- `-SemExportar`: pula o export, se você já exportou.
- `-Sim`: não pede confirmação.
- `-Branch outro`: usa outro branch de trabalho.

Se o PowerShell bloquear o script ("execução de scripts desabilitada"), rode uma vez:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Como o site funciona no ar

- Servidor: Oracle Cloud (OCI), Ubuntu, máquina `servicesbi-vm`, IP `168.75.87.24`.
- Acesso: `ssh -i ~/.ssh/servicesbi_oci ubuntu@168.75.87.24`.
- Nginx: `/etc/nginx/sites-enabled/servicesbi`.
  - `/` e `/static/` → arquivos prontos em `/home/ubuntu/site_servicesbi/cloudflare_dist`.
  - `/sige/` e `/sige-demo/` → Django do SIGE (outro projeto, em `/home/ubuntu/SIGE_ServicesBI`).
  - `/admin/` → Django do site (gunicorn.sock).
- DNS na Cloudflare, sem proxy: o domínio aponta direto para o servidor.
- O GitHub **não** publica sozinho. O site só muda quando o servidor faz `git pull`.

## Passo a passo manual (se o script não puder ser usado)

1. Exportar: `python manage.py export_static_site`
2. Commit e push do branch:
   ```
   git add -A
   git commit -m "mensagem"
   git push origin servicesbi-2.0
   ```
3. Atualizar a main:
   ```
   git checkout main
   git merge --ff-only servicesbi-2.0
   git push origin main
   git checkout servicesbi-2.0
   ```
4. Servidor:
   ```
   ssh -i ~/.ssh/servicesbi_oci ubuntu@168.75.87.24
   cd /home/ubuntu/site_servicesbi
   git pull --ff-only origin main
   ```
   Não precisa reiniciar o Nginx.
5. Conferir: `curl.exe -sI https://servicesbi.com.br`. O `Last-Modified` deve ser de hoje.

## Quando reiniciar o gunicorn

Só quando mudar código Python que o `/admin/` usa (settings, views, models) e você quiser que o `/admin/` pegue a mudança. O site público não precisa disso. No servidor: `sudo systemctl restart gunicorn`. Confira antes o nome do serviço com `systemctl list-units | grep gunicorn`.
