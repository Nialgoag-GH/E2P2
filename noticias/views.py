
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import News, Category

def noticias(request):
    # Obtener todas las noticias, ordenadas por fecha
    news = News.objects.all().order_by("-created")
    # Obtener todas las categorías
    categories = Category.objects.all().order_by("name")
    # Obtener el filtro enviado mediante GET
    category_id = request.GET.get("categoria")
    # Filtrar noticias cuando se selecciona una categoría
    if category_id:
        if not category_id.isdigit():
            raise Http404("Categoría no válida")

        category = get_object_or_404(
            Category,
            id=category_id
        )

        news = news.filter(categories=category)
    # Paginación de 3 noticias por página
    paginator = Paginator(news, 3)
    page_number = request.GET.get("page")
    news = paginator.get_page(page_number)
    
    return render(request, "noticias/noticias.html", {
        "news": news,
        "categories": categories,
        "selected_category": category_id
    })

def category(request, category_id):
    category = get_object_or_404(
        Category,
        id=category_id
    )

    return render(request, "noticias/category.html", {
        "category": category
    })
