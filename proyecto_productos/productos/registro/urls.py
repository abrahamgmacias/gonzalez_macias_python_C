from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registrar/", views.setProducto, name="registrar-producto"),
]