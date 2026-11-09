
from .models import News, Category


def informacion_sitio(request):
    return {
        "nombre_sitio": "VideoGames News",
        "total_noticias": News.objects.count(),
        "total_categorias": Category.objects.count(),
    }
