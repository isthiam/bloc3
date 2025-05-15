from django.db import models

class Offre(models.Model):
    SOLO = 1
    DUO = 2
    FAMILLE = 4
    CHOIX = [(SOLO, "Solo"), (DUO, "Duo"), (FAMILLE, "Famille")]

    nom = models.IntegerField(choices=CHOIX)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_nom_display()
