from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    cle_securite = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
