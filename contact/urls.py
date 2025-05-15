from django.urls import path
from . import views

urlpatterns = [
    path('', views.nous_contacter, name='nous_contacter'),
]
