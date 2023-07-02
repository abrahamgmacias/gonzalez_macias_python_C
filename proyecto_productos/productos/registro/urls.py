from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registrar/", views.setProducto, name="registrar-producto"),
    path("registrar/success/", views.successProducto, name="success-producto"),
    path("registrar/failure/", views.errorProducto, name="failure-producto"),
]