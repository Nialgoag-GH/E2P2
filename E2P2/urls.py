
from django.contrib import admin
from django.urls import path
from core import views as core_views
from about import views as about_views
from faq import views as faq_views
from noticias import views as noticias_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name="index"),
    path('about/', about_views.about, name="about"),
    path('faq/', faq_views.faq, name="faq"),
    path('noticias/', noticias_views.noticias, name="noticias")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)