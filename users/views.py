from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.shortcuts import render
from tickets.models import Reservation
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Votre compte a été créé avec le nom d'utilisateur : {user.username}")
            return redirect('mon_compte')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or 'mon_compte'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'users/logout_confirmation.html')




@login_required
def mon_compte(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'users/mon_compte.html', {'reservations': reservations})


@login_required
def edit_profil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mon_compte')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profil.html', {'form': form})