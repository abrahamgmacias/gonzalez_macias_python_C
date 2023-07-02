from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    data = Producto.objects.all()
    template = loader.get_template('productos.html')
    
    return HttpResponse(template.render(
        context={ "productos": data }, 
        request=request
        )
    )

def getProducto(request):
    if request.method == "GET":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            return HttpResponseRedirect("/submit/")

    if request.method == "POST":
        productoForm = ProductoForm()

    return render(request, "registerForm.html", {"form": productoForm})