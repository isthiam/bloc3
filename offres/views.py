from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from tickets.models import Reservation
from .models import Offre

def liste_offres(request):
    offres = Offre.objects.all()
    return render(request, 'offres/liste_offres.html', {'offres': offres})

def detail_offre(request, offre_id):
    offre = get_object_or_404(Offre, pk=offre_id)
    return render(request, 'offres/detail_offre.html', {'offre': offre})



def ajouter_au_panier(request, offre_id):
    panier = request.session.get('panier', [])
    panier.append(offre_id)
    request.session['panier'] = panier
    return redirect('liste_offres')

def voir_panier(request):
    panier = request.session.get('panier', [])
    offres = Offre.objects.filter(id__in=panier)
    return render(request, 'offres/panier.html', {'offres': offres})

def vider_panier(request):
    request.session['panier'] = []
    return redirect('voir_panier')


@login_required
def valider_panier(request):
    panier = request.session.get('panier', [])
    if not panier:
        return redirect('voir_panier')

    for offre_id in panier:
        offre = get_object_or_404(Offre, pk=offre_id)
        Reservation.objects.create(utilisateur=request.user, offre=offre)

    request.session['panier'] = []
    return render(request, 'offres/panier_valide.html')

@login_required
def paiement_panier(request):
    panier = request.session.get('panier', [])
    offres = Offre.objects.filter(id__in=panier)

    mode_paiement = request.POST.get('mode_paiement') if request.method == 'POST' else None

    if request.method == 'POST' and 'valider_paiement' in request.POST:
        for offre in offres:
            Reservation.objects.create(utilisateur=request.user, offre=offre)
        request.session['panier'] = []
        return render(request, 'offres/panier_valide.html', {'mode_paiement': mode_paiement})

    return render(request, 'offres/paiement_etapes.html', {'offres': offres, 'mode_paiement': mode_paiement})
