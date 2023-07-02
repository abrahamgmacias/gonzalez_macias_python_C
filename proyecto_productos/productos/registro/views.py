from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Producto
from .forms import registroProductoForm

# Create your views here.
def index(request):
    data = Producto.objects.all()
    template = loader.get_template('productos.html')
    
    return HttpResponse(template.render(
        context={ "productos": data }, 
        request=request
        )
    )

def setProducto(request):
    form = registroProductoForm()
    return render(request, 'registrarProducto.html', {"form": form})