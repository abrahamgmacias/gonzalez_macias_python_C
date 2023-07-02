from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, )
    descripcion = forms.CharField(max_length=200, )
    precio = forms.IntegerField()
    fecha_de_registro = forms.DateField()
    estatus = forms.CharField(
        max_length=100
    )