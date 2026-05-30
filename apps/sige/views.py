from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def sige_entry(request):
    if request.user.is_authenticated:
        return redirect("sige:dashboard")
    return redirect("sige:login")


@login_required
def dashboard(request):
    return render(request, "sige/dashboard.html")
