from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from tickets.views import statistiques_ventes

# Vue de test pour l'accueil


def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('', home),  # Route pour l'accueil
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('offres/', include('offres.urls')),
    path('tickets/', include('tickets.urls')),
    path('contact/', include('contact.urls')),
    path('tickets/', include('tickets.urls')),
    path('statistiques/', statistiques_ventes, name='statistiques_ventes'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

