from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . forms import UserRegisterForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method != 'POST':
        # mandar el forlumario vacio, comportamiento default
        return render(request, 'register.html', {
            'form' : UserRegisterForm()
        })

    # recuperar los datos del formulario
    form = UserRegisterForm(request.POST)

    if not form.is_valid():
        # mostrar el formulario con  errores
        return render(request, 'register.html', {
            'form' : form
        })
    
    # guardar el registro
    form.save()
    return redirect('dashboard')


@login_required
def dashboard(request):
    user = User.objects.get(
        username = request.user.username
    )

    # grupos creados por el usuario
    user_groups = user.group_admin.all()

    # grupos a los que el usuario pertenece
    user_member = user.group_member.all()

    return render(request, 'dashboard.html', context={
        'user_groups': user_groups,
        'user_member': user_member
    })


# crear grupos

# elimiar grupos

# agregar a un grupo

# eliminar de un grupo

# hacer formulario de belbin
