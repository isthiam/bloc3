from django.db import models
from django.conf import settings
from offres.models import Offre
import uuid
import qrcode
from io import BytesIO
from django.core.files import File

class Reservation(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    cle_reservation = models.UUIDField(default=uuid.uuid4, editable=False)
    cle_finale = models.CharField(max_length=255, blank=True)  # ✅ Allongé à 255
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='en_attente')

    def save(self, *args, **kwargs):
        if not self.cle_finale:
            # ✅ Correction ici avec cle_securite
            self.cle_finale = f"{self.utilisateur.cle_securite}-{self.cle_reservation}"
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        qr = qrcode.make(self.cle_finale)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f'qrcode_{self.utilisateur.id}_{self.cle_reservation}.png'
        self.qrcode.save(file_name, File(buffer), save=False)
