from django.urls import path

from . import views


app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("sige-servicesbi/", views.sige_institucional_page, name="sige_institucional"),
    path("jarvis/", views.jarvis_page, name="jarvis"),
    path("python/", views.python_page, name="python"),
    path("power-bi/", views.powerbi_page, name="powerbi"),
    path("automacoes/", views.automacoes_page, name="automacoes"),
    path("excel/", views.excel_page, name="excel"),
    path("curriculo/", views.curriculo_page, name="curriculo"),
    path("contato/", views.contato_page, name="contato"),
]
