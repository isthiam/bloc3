from django.urls import path
from . import views
from .views import valider_qrcode

urlpatterns = [
    path('reserver/<int:offre_id>/', views.reserver_offre, name='reserver_offre'),
    path('paiement/<int:reservation_id>/', views.simuler_paiement, name='simuler_paiement'),
    path('valider/', views.valider_qrcode, name='valider_qrcode'),
    path('billet/<int:reservation_id>/', views.telecharger_billet, name='telecharger_billet'), 
    path('valider_qrcode/', valider_qrcode, name='valider_qrcode'),
    path('scanner/', views.interface_valider_billet, name='interface_valider_billet'),

]
