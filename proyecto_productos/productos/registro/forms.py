from django import forms
from .models import Producto

class registroProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'estatus') 
