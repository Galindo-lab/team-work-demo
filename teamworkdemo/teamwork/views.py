from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . models import Group
from . forms import UserRegisterForm, CreateGroupForm


def home(request):
    # pagina de inicio
    return render(request, 'home.html')


def register(request):
    if request.method != 'POST':
        # mandar el formulario vacio, comportamiento default
        return render(request, 'register.html', {
            'form': UserRegisterForm()
        })

    # recuperar los datos del formulario
    form = UserRegisterForm(request.POST)

    if not form.is_valid():
        # mostrar el formulario con  errores
        return render(request, 'register.html', {
            'form': form
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


@login_required
def create_group(request):
    # mandar el formulario vacio
    if request.method != 'POST':
        return render(request, 'create_group.html', {
            'form': CreateGroupForm()
        })

    # recuperar los datos del formulario
    form = CreateGroupForm(request.POST)

    if not form.is_valid():
        return render(request, 'create_group.html', {
            'form': form
        })

    # verificar que el nombre sea unico
    group = Group.objects.filter(
        name = form.cleaned_data['name'],
        admin = request.user
    )

    if group.exists():
        form.add_error('name', 'Ya existe ese registro')

        return render(request, 'create_group.html', {
            'form': form
        })

    # guardar el registro
    group_register = form.save(commit=False)
    group_register.admin = request.user
    group_register.save()

    return redirect('dashboard')

# elimiar grupos

# agregar a un grupo

# eliminar de un grupo

# hacer formulario de belbin
