from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import registroProductoForm
from django.template import loader
from .models import Producto
from django.utils import timezone


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
    if request.method == "POST":
        form = registroProductoForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_de_registro = timezone.now()
            post.save()
            return redirect('success-producto')

        else:
            return redirect('failure-producto')
    
    else:
        form = registroProductoForm()

    return render(request, 'registrarProducto.html', {"form": form})

def successProducto(request):
    return HttpResponse("El producto ha sido registrado con éxito.")

def errorProducto(request):
    return HttpResponse("Ha sucedido un error al registrar el producto. Intente de nuevo.")