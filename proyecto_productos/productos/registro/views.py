from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Producto

# Create your views here.
def index(request):
    data = Producto.objects.all()
    template = loader.get_template('productos.html')
    
    return HttpResponse(template.render(
        context={ "productos": data }, 
        request=request
        )
    )