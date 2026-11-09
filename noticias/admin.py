
from django.contrib import admin
from .models import News, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "updated")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("created", "updated")
    list_per_page = 10


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "updated")
    list_display_links = ("id", "title")
    list_filter = ("categories", "created")
    search_fields = ("title", "detail")
    ordering = ("-created",)
    readonly_fields = ("created", "updated")
    list_per_page = 10
    filter_horizontal = ("categories",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "news", "created")
    list_display_links = ("id", "name")
    list_filter = ("created", "news")
    search_fields = ("name", "content", "news__title")
    ordering = ("-created",)
    readonly_fields = ("created",)
    list_per_page = 10

#atrivutos presonalizados 
#Atributo	            Función
#list_display	        Muestra ID, título y fechas
#list_display_links	    Permite abrir una noticia desde su ID o título
#list_filter	        Filtra noticias por categoría y fecha
#search_fields	        Busca por título y descripción
#ordering	            Muestra primero las noticias más recientes
#readonly_fields	    Impide modificar manualmente las fechas
#list_per_page	        Muestra diez noticias por página
#filter_horizontal	    Permite seleccionar varias categorías fácilmente