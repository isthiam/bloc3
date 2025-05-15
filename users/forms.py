from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="Prénom")
    last_name = forms.CharField(required=True, label="Nom")

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Génère le username automatiquement : prénomnom en minuscules sans espace
        user.username = f"{self.cleaned_data['first_name']}{self.cleaned_data['last_name']}".replace(" ", "").lower()
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
