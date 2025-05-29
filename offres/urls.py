from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.liste_offres, name='liste_offres'),
    path('<int:offre_id>/', views.detail_offre, name='detail_offre'),
    path('ajouter/<int:offre_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('panier/vider/', views.vider_panier, name='vider_panier'),
    path('panier/valider/', views.valider_panier, name='valider_panier'),
    path('panier/paiement/', views.paiement_panier, name='paiement_panier'),


]

