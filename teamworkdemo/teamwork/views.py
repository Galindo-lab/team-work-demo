from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . forms import UserRegisterForm


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        else:
            return render(request, 'register.html', context={
                'form' : form
            })

    else:
        return render(request, 'register.html', contex={
            'form' : UserRegisterForm()
        })


@login_required
def dashboard(request):
    user = User.objects.get(
        username = request.user.username
    )

    user_groups = user.admin.all()
    user_member = user.part_of.all()

    return render(request, 'dashboard.html', context={
        'user_groups': user_groups,
        'user_member': user_member
    })


# crear grupos

# elimiar grupos

# agregar a un grupo

# eliminar de un grupo

# hacer formulario de belbin
