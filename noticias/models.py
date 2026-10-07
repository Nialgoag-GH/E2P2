from django.db import models


class News(models.Model):
    opcion_categoria = [
        'LANZAMIENTOS',
        'INDUSTRIA',
        'EVENTOS',
        'ACTUALIZACIONES'
    ]

    title = models.CharField(max_length=100, verbose_name="Titulo")
    detail = models.TextField(verbose_name="Detalle")
    category = models.CharField(
        max_length=20,
        choices=[(categoria, categoria) for categoria in opcion_categoria],
        verbose_name="Categoría"
    )
    image = models.ImageField(upload_to="mynews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.title


