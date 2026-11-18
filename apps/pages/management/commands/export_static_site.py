import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.test import Client, override_settings

PAGES = [
    ("/", "index.html"),
    ("/consultoria-financeira/", "consultoria-financeira/index.html"),
    ("/sobre/", "sobre/index.html"),
    ("/sige-servicesbi/", "sige-servicesbi/index.html"),
    ("/jarvis/", "jarvis/index.html"),
    ("/python/", "python/index.html"),
    ("/power-bi/", "power-bi/index.html"),
    ("/automacoes/", "automacoes/index.html"),
    ("/excel/", "excel/index.html"),
    ("/curriculo/", "curriculo/index.html"),
    ("/contato/", "contato/index.html"),
    ("/robots.txt", "robots.txt"),
    ("/sitemap.xml", "sitemap.xml"),
]


class Command(BaseCommand):
    help = "Exporta o site Django como HTML estático para cloudflare_dist/"

    @override_settings(ALLOWED_HOSTS=["*"])
    def handle(self, *args, **options):
        dist: Path = settings.BASE_DIR / "cloudflare_dist"
        static_src: Path = settings.BASE_DIR / "static"

        if dist.exists():
            shutil.rmtree(dist)
        dist.mkdir()

        client = Client()
        results = []

        self.stdout.write("\n=== Exportando páginas ===\n")

        for url, output_path in PAGES:
            response = client.get(url)
            status = response.status_code

            if status != 200:
                raise CommandError(
                    f"FALHA: rota {url!r} retornou HTTP {status}. Export abortado."
                )

            out_file = dist / output_path
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_bytes(response.content)

            results.append((status, url, output_path))
            self.stdout.write(f"  [{status}] {url:30s} -> {output_path}")

        self.stdout.write("\n=== Copiando static/ ===\n")
        shutil.copytree(static_src, dist / "static")
        self.stdout.write("  static/ -> cloudflare_dist/static/\n")

        self.stdout.write("=== Relatório final ===\n")
        for status, url, path in results:
            self.stdout.write(f"  {status}  {url:30s}  ->  cloudflare_dist/{path}")

        total = len(results)
        self.stdout.write(
            f"\nOK: {total} pagina(s) exportada(s). Saida: {dist}\n"
        )
