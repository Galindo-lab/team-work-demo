from django.urls import path

from core.views import FormView

urlpatterns = [
    path(
        route='',
        name='index',
        view=FormView.as_view()
    ),
]
