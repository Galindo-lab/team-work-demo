from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    
    return render(request, 'register.html', {
        'form': UserRegisterForm()
    })


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# crear grupos

# elimiar grupos

# agregar a un grupo

# eliminar de un grupo

# hacer formulario de belbin
