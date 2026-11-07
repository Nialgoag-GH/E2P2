from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import News, Category

def noticias(request):
    news = News.objects.all().order_by("-created") #Hace que las noticias más recientes aparezcan primero
    paginator = Paginator(news,3) #paginacion de 3 noticias por pagina
    page_number = request.GET.get("page")
    news = paginator.get_page(page_number)
    return render(request,"noticias/noticias.html",{'news':news})

def category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    return render(request,"noticias/category.html", {'category':category})