from django.urls import path

urlpatterns = [
    path(
        route='',
        name='index',
        view=FormView.as_view()
    ),
]
