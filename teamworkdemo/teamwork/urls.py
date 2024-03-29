from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

from . import views
from . forms import UserLoginForm

urlpatterns = [
    # login
    path('login/', LoginView.as_view(
        template_name='login.html',
        authentication_form=UserLoginForm
    ), name='login'),

    # logout
    path('logout/', LogoutView.as_view(), name='logout'),

    # url patterns
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # group
    # path('create/', views.create_group, name='create'),
    path('delete/<int:group_id>', views.delete_group, name='delete'),
    path('details/<int:group_id>', views.group_details, name='details'),
    path('invitation/<str:username>/<str:group_name>',
         views.invitation_request, name='invitation'),
    path('remove/<int:integrante_id>', views.remove_member, name='remove'),
    path('join/<str:username>/<str:group_name>', views.join_group, name='join'),
    path('form/<str:admin_username>/<str:group_name>',
         views.belbin_form, name='form'),
    path('results/<str:username>/<str:group_name>',
         views.form_results, name='results')

]
