from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Nombre Categoria")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    detail = models.TextField(verbose_name="Detalle")
    image = models.ImageField(upload_to="mynews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, verbose_name="Categorías")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE,related_name="comments",verbose_name="Noticia")  #relaciona cada comentario con una noticia.
    name = models.CharField(max_length=100,verbose_name="Nombre del autor")
    content = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    
    def __str__(self):
        return f"{self.name} - {self.news.title}"



