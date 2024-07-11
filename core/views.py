from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import JoinGroupForm
from .models import Group, EvaluationResult


class JoinGroupView(LoginRequiredMixin, View):
    def get(self, request, name=None):
        form = JoinGroupForm(initial={'group': get_object_or_404(Group, name=name)})

        return render(
            request=request,
            template_name='join_group.html',
            context={'form': form}
        )

    def post(self, request, name=None):
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            user = request.user

            # Verificar si el usuario ya es miembro del grupo
            if EvaluationResult.objects.filter(group=group, user=user).exists():
                messages.warning(request, "Ya eres miembro de este grupo.")
            else:
                # Crear el EvaluationResult para asociar el usuario al grupo
                EvaluationResult.objects.create(group=group, user=user)
                messages.success(request, f"Te has unido al grupo {group.name}.")
            return redirect('groups')  # Redirigir a una vista apropiada después de unirse

        return render(request, 'join_group.html', {'form': form})


class GroupListView(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request=request,
            template_name='groups_list.html',
            context={
                'groups': Group.objects.all()
            }
        )

    def post(self, request):
        pass
