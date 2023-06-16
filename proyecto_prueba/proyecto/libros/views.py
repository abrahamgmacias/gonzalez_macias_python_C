from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Libros

def index(request):
    return HttpResponse("Something")

class Inicio(View):
    template_name = 'index.html'

    def post():
        return

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def insertar_libro(request):
    nuevo_l