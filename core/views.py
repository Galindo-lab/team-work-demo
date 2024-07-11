from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .models import Group


class JoinGroupView(LoginRequiredMixin, View):
    def get(self, request, name=None):
        pass

    def post(self, request):
        pass


class GroupListView(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request=request,
            template_name='join_group.html',
            context={
                'groups': Group.objects.all()
            }
        )

    def post(self, request):
        pass
