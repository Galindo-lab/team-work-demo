from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from . models import Group, Integrante, Member, BelbinUserProfile
from . forms import UserRegisterForm, CreateGroupForm, BelbinForm


def home(request):
    # pagina de inicio
    return render(request, 'home.html')


def register(request):
    if request.method != 'POST':
        # mandar el formulario vacio
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
        username=request.user.username
    )

    # grupos creados por el usuario
    user_groups = user.group_admin.all()

    # grupos a los que el usuario pertenece
    user_member = user.group_member.all()

    return render(request, 'dashboard.html', {
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
    # https://stackoverflow.com/a/30049925/22015904
    group = Group.objects.filter(
        name=form.cleaned_data['name'],
        admin=request.user
    )

    if group.exists():
        # https://stackoverflow.com/a/60258267/22015904
        form.add_error('name', 'Ya existe ese registro')

        return render(request, 'create_group.html', {
            'form': form
        })

    # guardar el registro
    # https://stackoverflow.com/a/12848678/22015904
    group_register = form.save(commit=False)
    group_register.admin = request.user
    group_register.save()

    return redirect('dashboard')


@login_required
def delete_group(request, group_id):
    post = Group.objects.get(id=group_id)
    post.delete()
    return redirect('dashboard')


@login_required
def group_details(request, group_id):
    # TODO: cambiar el 'group_id' con 'group_name'

    group = Group.objects.get(id=group_id)
    members = Integrante.objects.filter(group=group)

    return render(request, 'group_details.html', {
        'group': group,
        'members': members
    })


def invitation_request(request, username, group_name):
    # TODO: Agregar contraseña para los formularios

    # https://stackoverflow.com/a/44386827/22015904
    user = get_object_or_404(User, username=username)
    group = get_object_or_404(Group, name=group_name, admin=user)

    if not request.user.is_authenticated:
        # mostrar la pantalla con el mensaje de iniciar sesion
        return render(request, 'join_group.html', {
            'group': group
        })

    integrante = Integrante.objects.filter(
        member=request.user,
        group=group
    )

    # mostrar el estado
    return render(request, 'join_group.html', {
        'group': group,
        'integrante': integrante
    })


@login_required
def join_group(request,  username, group_name):
    user = get_object_or_404(User, username=username)
    group = get_object_or_404(Group, name=group_name, admin=user)

    integrante = Integrante(
        member=user,
        group=group
    )

    integrante.save()

    # TODO: Rediregir al formulario de Belbin
    return redirect('dashboard')


@login_required
def remove_member(request, integrante_id):
    member = Integrante.objects.get(id=integrante_id)
    member.delete()
    return redirect('dashboard')


@login_required
def belbin_form(request, username, group_name):
    user = get_object_or_404(User, username=username)
    group = get_object_or_404(Group, name=group_name, admin=user)

    integrante = get_object_or_404(
        Integrante, 
        member=request.user, 
        group=group
    )

    belbin_form = BelbinUserProfile.objects.filter(
        integrante=integrante
    )

    if request.method != 'POST':
        # Mandar formulario vacio
        return render(request, 'form.html', {
            'form': BelbinForm(),
            'integrante': integrante,
            'belbin_form': belbin_form
        })

    # form = CreateGroupForm(request.POST)

    # group_register = form.save(commit=False)
    # group_register.admin = request.user
    # group_register.save()

    return HttpResponse("Nada")
