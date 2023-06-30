from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField("Titulo", max_length=300, default="Sin titulo")
    edicion = models.CharField("Titulo", max_length=300, default="Sin edicion")
    editorial = models.CharField("Titulo", max_length=300, default="Sin editorial")
    año_de_publicacion = models.CharField("Titulo", max_length=300, default="Sin año de publicación")
    pagina = models.IntegerField("Pagina", default=0)

    class Meta:
        verbose_name = "Libros"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo