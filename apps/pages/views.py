from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def python_page(request):
    return render(request, "pages/python.html")


def powerbi_page(request):
    return render(request, "pages/powerbi.html")


def automacoes_page(request):
    return render(request, "pages/automacoes.html")


def excel_page(request):
    return render(request, "pages/excel.html")


def curriculo_page(request):
    return render(request, "pages/curriculo.html")


def contato_page(request):
    return render(request, "pages/contato.html")
