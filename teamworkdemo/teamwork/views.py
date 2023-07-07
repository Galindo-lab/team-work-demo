from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from . models import Group
from . models import Member
from . models import Profile
from . models import BelbinUserProfile

from . forms import UserRegisterForm
from . forms import CreateGroupForm
from . forms import BelbinForm


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
    # Mostrar el dashboard normal
    user = User.objects.get(
        username=request.user.username
    )

    # grupos creados por el usuario
    user_groups = user.group_admin.all()

    # grupos a los que el usuario pertenece
    user_member = user.group_member.all()

    if request.method != 'POST':
        # formulario vacio
        return render(request, 'dashboard.html', {
            'user_groups': user_groups,
            'user_member': user_member,
            'creteGroupForm': CreateGroupForm()
        })

    # recuperar los datos del formulario
    form = CreateGroupForm(request.POST)

    if not form.is_valid():
        return render(request, 'dashboard.html', {
            'user_groups': user_groups,
            'user_member': user_member,
            'creteGroupForm': form
        })

    # verificar que el nombre sea unico
    # https://stackoverflow.com/a/30049925/22015904
    group = Group.objects.filter(
        name=form.cleaned_data['name'],
        admin=request.user
    )

    if group.exists():
        # https://stackoverflow.com/a/60258267/22015904
        form.add_error('name', 'Ya existe un grupo con ese nombre')

        return render(request, 'dashboard.html', {
            'user_groups': user_groups,
            'user_member': user_member,
            'creteGroupForm': form
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
    members = Member.objects.filter(group=group)

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

    integrante = Member.objects.filter(
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

    member = Member.objects.filter(
        member=request.user,
        group=group
    )

    if not member.exists():
        integrante = Member(
            member=request.user,
            group=group
        )

        integrante.save()

    # mandarte directo al formulario
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_member(request, integrante_id):
    member = Member.objects.get(id=integrante_id)

    belbin_form = BelbinUserProfile.objects.filter(
        member=member.member,
        group=member.group
    )

    if belbin_form.exists():
        # TODO: buscar una mejor forma de hacer esto
        # NOTE: quiza se puede agregar el miembro al modelo para eliminar todo en cascada
        form = BelbinUserProfile.objects.get(
            member=member.member,
            group=member.group
        )

        form.delete()

    member.delete()

    # https://stackoverflow.com/a/35796330/22015904
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def belbin_form(request, admin_username, group_name):
    admin_user = get_object_or_404(
        User,
        username=admin_username
    )

    group = get_object_or_404(
        Group,
        name=group_name,
        admin=admin_user
    )

    member = get_object_or_404(
        Member,
        member=request.user,
        group=group
    )

    belbin_form = BelbinUserProfile.objects.filter(
        member=request.user,
        group=group
    )

    if belbin_form.exists():
        # si ya se resolvio el formulario mostrar los resultados
        # https://stackoverflow.com/a/66828392/22015904
        return redirect(
            'results',
            username=admin_username,
            group_name=group_name
        )

    if request.method != 'POST':
        # Mandar formulario vacio
        return render(request, 'form.html', {
            'form': BelbinForm(),
            'belbin_form': belbin_form
        })

    # capturar el formulario
    form = BelbinForm(request.POST)

    if not form.is_valid():
        # si el formulario es invalido mostrar error
        return render(request, 'form.html', {
            'form': form,
            'belbin_form': belbin_form
        })

    # guardar el formulario
    form_save = form.save(commit=False)
    form_save.member = request.user
    form_save.group = group
    form_save.save()

    return redirect('dashboard')


@login_required
def form_results(request, username, group_name):
    user = get_object_or_404(
        User,
        username=username
    )

    group = get_object_or_404(
        Group,
        name=group_name,
        admin=user
    )

    belbin_form = BelbinUserProfile.objects.get(
        member=request.user,
        group=group
    )

    return render(request, 'results.html', {
        'profile': belbin_form
    })
