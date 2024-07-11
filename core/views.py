from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.detail import DetailView

from .forms import JoinGroupForm
from .models import Group, EvaluationResult


class JoinGroupView(LoginRequiredMixin, View):

    def get(self, request, name=None):
        group = get_object_or_404(Group, name=name)

        if EvaluationResult.objects.filter(group=group, user=self.request.user).exists():
            return redirect('group_detail', pk=group.pk)

        return render(
            request=request,
            template_name='join_group.html',
            context={'form': JoinGroupForm(initial={'group': group})}
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
            return redirect('group_detail', pk=group.pk)  # Redirigir a una vista apropiada después de unirse

        return render(request, 'join_group.html', {'form': form})


class GroupDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Group
    template_name = 'group_detail.html'
    context_object_name = 'group'

    def test_func(self):
        group = get_object_or_404(Group, name=self.get_object())
        return EvaluationResult.objects.filter(group=group, user=self.request.user).exists()

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para ver los detalles de este grupo.")

        # TODO: mensaje de error
        return redirect('groups_list')


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
