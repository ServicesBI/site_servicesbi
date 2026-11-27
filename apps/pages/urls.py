from django.urls import path

from . import central, views


app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("consultoria-financeira/", views.consultoria_page, name="consultoria"),
    path("sobre/", views.sobre_page, name="sobre"),
    path("sige-servicesbi/", views.sige_institucional_page, name="sige_institucional"),
    path("jarvis/", views.jarvis_page, name="jarvis"),
    path("python/", views.python_page, name="python"),
    path("power-bi/", views.powerbi_page, name="powerbi"),
    path("produtos/", views.produtos_page, name="produtos"),
    path("produtos/sige/", views.sige_produto_page, name="sige_produto"),
    path("cases/", views.cases_page, name="cases"),
    path("automacoes/", views.automacoes_page, name="automacoes"),
    path("excel/", views.excel_page, name="excel"),
    path("curriculo/", views.curriculo_page, name="curriculo"),
    path("contato/", views.contato_page, name="contato"),
    path("robots.txt", views.robots_txt, name="robots"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap"),
    # Central de comando: só funciona no PC (runserver local). Ver apps/pages/central.py
    path("central/status/", central.central_status, name="central_status"),
    path("central/exportar/", central.central_exportar, name="central_exportar"),
    path("central/publicar/", central.central_publicar, name="central_publicar"),
    path("central/publicar/status/", central.central_publicar_status, name="central_publicar_status"),
]
