from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "sige"

urlpatterns = [
    path("", views.sige_entry, name="entry"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="sige/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout",
    ),
    path("dashboard/", views.dashboard, name="dashboard"),
]
