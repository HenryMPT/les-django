"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="homepage"),
    path("adminarea", views.home, name="adminarea"),
    path("utilizadores", views.utilizadores, name="utilizadores"),
    path("utilizadores/UserDelete/<int:pk>", views.UserDelete.as_view(success_url=('/utilizadores')),  name="UserDelete"),
    path("utilizadores/UserUpdate/<int:pk>", views.UserUpdate.as_view(success_url=('/utilizadores')),  name="UserUpdate"),
    path("empresas", views.empresas, name="empresas"),
    path("empresas/OrganizationCreate", views.OrganizationCreate.as_view(success_url=('/empresas')), name="empresas"),
    path("empresas/OrganizationDelete/<int:pk>", views.OrganizationDelete.as_view(success_url=('/empresas')),  name="OrganizationDelete"),
     path("empresas/OrganizationUpdate/<int:pk>", views.OrganizationUpdate.as_view(success_url=('/empresas')),  name="OrganizationUpdate"),
    path("register", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("login2", views.login2_request, name="login2"),
    path("gparea", views.gparea, name="gparea"),
    path("processos", views.processos, name="processos"),
    path("processos/ProcessCreate", views.ProcessCreate.as_view(success_url=('/processos')), name="ProcessCreate"),
    path("processos/ProcessUpdate/<int:pk>", views.ProcessUpdate.as_view(success_url=('/processos')), name="ProcessUpdate"),
    path("processos/ProcessDelete/<int:pk>", views.ProcessDelete.as_view(success_url=('/processos')), name="ProcessDelete"),
    path("actividades", views.actividades, name="actividades"),
    path("actividades/ActivityCreate", views.ActivityCreate.as_view(success_url=('/actividades')), name="ActivityCreate"),
    path("actividades/ActivityUpdate/<int:pk>", views.ActivityUpdate.as_view(success_url=('/processos')), name="ProcessUpdate"),
    path("actividades/ActivityDelete/<int:pk>", views.ActivityDelete.as_view(success_url=('/processos')), name="ProcessDelete"),
]
