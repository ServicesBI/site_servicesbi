from django.shortcuts import redirect


def sige_entry(request):
    return redirect("sige:login")
