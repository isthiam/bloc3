from django.test import TestCase
from django.contrib.auth import get_user_model
from offres.models import Offre
from .models import Reservation

class ReservationTestCase(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='motdepasse')
        self.offre = Offre.objects.create(nom=1, description='Solo', prix=50)

    def test_reservation_creation(self):
        reservation = Reservation.objects.create(utilisateur=self.user, offre=self.offre)
        self.assertTrue(reservation.cle_finale)

