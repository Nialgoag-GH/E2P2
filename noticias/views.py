from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

def noticias(request):
    news=News.objects.all()
    paginator = Paginator(news,3)
    page_number = request.GET.get("page")
    news = paginator.get_page(page_number)
    return render(request,"noticias/noticias.html")
