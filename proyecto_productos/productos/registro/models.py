from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(null=False)
    descripcion = models.CharField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_registro = models.DateField(null=False)
    estatus = models.CharField(null=False)

    def __str__(self):
        return self.nombre