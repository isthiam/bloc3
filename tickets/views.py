from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import Reservation
from offres.models import Offre

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Reservation


from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from offres.models import Offre
from tickets.models import Reservation

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render



@login_required
def valider_qrcode(request):
    if request.method == 'POST':
        cle_finale = request.POST.get('cle_finale')
        try:
            reservation = Reservation.objects.get(cle_finale=cle_finale)
            if reservation.statut == 'en_attente':
                reservation.statut = 'valide'
                reservation.save()
                return JsonResponse({'status': 'success', 'message': 'Billet valide.'})
            elif reservation.statut == 'valide':
                return JsonResponse({'status': 'warning', 'message': 'Billet déjà scanné.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Statut invalide.'})
        except Reservation.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Billet non reconnu.'})
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée.'})



@login_required
def reserver_offre(request, offre_id):
    offre = get_object_or_404(Offre, pk=offre_id)
    reservation = Reservation.objects.create(utilisateur=request.user, offre=offre)
    return redirect('simuler_paiement', reservation_id=reservation.id)





@login_required
@csrf_protect
def simuler_paiement(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, utilisateur=request.user)
    
    if request.method == 'POST':
        reservation.statut = 'payé'
        reservation.save()
        return render(request, 'tickets/confirmation.html', {'reservation': reservation})
    
    return render(request, 'tickets/simuler_paiement.html', {'reservation': reservation})





@login_required
def telecharger_billet(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, utilisateur=request.user)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, f"Billet pour : {reservation.offre.get_nom_display()}")
    p.setFont("Helvetica", 12)
    p.drawString(100, 780, f"Réservé par : {reservation.utilisateur.username}")
    p.drawString(100, 760, f"Statut : {reservation.statut}")
    #p.drawString(100, 740, f"Clé de sécurité : {reservation.cle_finale}")

    # Ajout du QR Code si disponible
    if reservation.qrcode:
        from reportlab.lib.utils import ImageReader
        p.drawImage(ImageReader(reservation.qrcode.path), 100, 600, width=150, height=150)

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')



@staff_member_required
def valider_qrcode(request):
    if request.method == 'POST':
        cle_finale = request.POST.get('cle_finale')
        try:
            reservation = Reservation.objects.get(cle_finale=cle_finale)
            return JsonResponse({
                'status': 'valid',
                'message': f'Billet authentique pour {reservation.utilisateur.username}',
                'statut': reservation.statut
            })
        except Reservation.DoesNotExist:
            return JsonResponse({'status': 'invalid', 'message': 'Billet non reconnu'})




@staff_member_required
def statistiques_ventes(request):
    stats = []
    for offre in Offre.objects.all():
        count = Reservation.objects.filter(offre=offre).count()
        stats.append({'offre': offre.get_nom_display(), 'nombre': count})
    return render(request, 'admin/statistiques_ventes.html', {'stats': stats})





@staff_member_required
def interface_valider_billet(request):
    return render(request, 'tickets/valider_billet.html')
