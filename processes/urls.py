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

app_name = "processes"

urlpatterns = [
    path("", views.home, name="homepage"),
    path("processos", views.processos, name="processos"),
    path("processos/ProcessCreate", views.ProcessCreate.as_view(success_url=('/processos')), name="ProcessCreate"),
    path("processos/ProcessUpdate/<int:pk>", views.ProcessUpdate.as_view(success_url=('/processos')), name="ProcessUpdate"),
    path("processos/ProcessDelete/<int:pk>", views.ProcessDelete.as_view(success_url=('/processos')), name="ProcessDelete"),
    path("processos/ProcessDetail/<int:pk>", views.ProcessDetail.as_view(), name="ProcessDetail"),
    path("actividades", views.actividades, name="actividades"),
    path("actividades/ActivityCreate", views.ActivityCreate.as_view(success_url=('/actividades')), name="ActivityCreate"),
    path("actividades/ActivityUpdate/<int:pk>", views.ActivityUpdate.as_view(success_url=('/actividades')), name="ActivityUpdate"),
    path("actividades/ActivityDelete/<int:pk>", views.ActivityDelete.as_view(success_url=('/actividades')), name="ActivityDelete"),
    path("actividades/ActivitySwap/<int:pk>/<int:fk>", views.ActivitySwap.as_view(success_url=('/actividades')), name="ActivitySwap"),
    path("produtos", views.produtos, name="produtos"),
    path("produtos/ProductCreate", views.ProductCreate.as_view(success_url=('/produtos')), name="ProductCreate"),
    path("produtos/ProductUpdate/<int:pk>", views.ProductUpdate.as_view(success_url=('/produtos')), name="ProductUpdate"),
    path("produtos/ProductDelete/<int:pk>", views.ProductDelete.as_view(success_url=('/produtos')), name="ProductDelete"),
    path("papeis", views.papeis, name="papeis"),
    path("papeis/RoleCreate", views.RoleCreate.as_view(success_url=('/papeis')), name="RoleCreate"),
    path("papeis/RoleUpdate/<int:pk>", views.RoleUpdate.as_view(success_url=('/papeis')), name="RoleUpdate"),
    path("papeis/RoleDelete/<int:pk>", views.RoleDelete.as_view(success_url=('/papeis')), name="RoleDelete"),
]

