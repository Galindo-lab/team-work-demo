from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Group, Integrante, Member
from . forms import UserRegisterForm, CreateGroupForm


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
    group = Group.objects.get(id=group_id)
    members = Integrante.objects.filter(group=group)

    return render(request, 'group_details.html', {
        'group': group,
        'members': members
    })


@login_required
def join_group(request,  username, group_name):
    # TODO: join_group
    pass


@login_required
def invitation_request(request, username, group_name):
    user = get_list_or_404(User, username=username)

    return HttpResponse(user)

    # user = User.objects.filter(
    #     username=username
    # )

    # if not user.exists():
    #     # TODO: agregar una pantalla de error
    #     return HttpResponse('Invitacion invalida')
    
    # member = Member.objects.filter(
    #     user=user
    # )

    # if not member.exists():
    #     # TODO: agregar una pantalla de error
    #     return HttpResponse('Invitacion invalida 2')

    # group = Group.objects.filter(
    #     name=group_name,
    #     admin=user
    # ).first()


    # return HttpResponse(group.exists())

    # return render(request, 'join_group.html', {
    #     'group': group,
    #     'is_member': member2.exists()
    # })


# eliminar miembro de un grupo

# salir de un grupo

# hacer formulario de belbin
