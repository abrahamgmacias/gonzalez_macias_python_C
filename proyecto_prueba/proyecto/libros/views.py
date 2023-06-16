from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Libro

def index(request):
    return HttpResponse("Something")

class Inicio(View):
    template_name = 'index.html'

    def post():
        return

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def insertar_libro(request):
    nuevo_libro = Libro(
        titulo="El Gran Libro",
        edicion="Primera edición", 
        editorial="Editorial", 
        año_de_publicacion="2009", 
        paginas=200
    )

    nuevo_libro.save()

    return HttpResponse("Libro insertado correctamente.")