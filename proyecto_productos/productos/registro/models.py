from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    precio = models.IntegerField(null=False)
    fecha_de_registro = models.DateField(null=False)
    estatus = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre