from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BelbinForm, JoinGroupForm
from .models import BelbinProfile, GroupForm


class FormView(CreateView):
    model = BelbinProfile
    form_class = BelbinForm
    template_name = 'belbin.html'
    success_url = reverse_lazy('yourmodel-list')


@login_required
def join_group(request):
    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            user = request.user

            # Verificar si el usuario ya es miembro del grupo
            if GroupForm.objects.filter(group=group, user=user).exists():
                messages.warning(request, "Ya eres miembro de este grupo.")
            else:
                # Crear el GroupForm para asociar el usuario al grupo
                GroupForm.objects.create(group=group, user=user)
                messages.success(request, f"Te has unido al grupo {group.name}.")
            return redirect('some_view_name')  # Redirigir a una vista apropiada después de unirse
    else:
        form = JoinGroupForm()

    return render(request, 'join_group.html', {'form': form})