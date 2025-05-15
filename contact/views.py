from django.shortcuts import render
from django.contrib import messages

def nous_contacter(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Simulation : afficher un message de confirmation
        messages.success(request, 'Votre demande a bien été envoyée. Merci !')
    return render(request, 'contact/contact.html')
