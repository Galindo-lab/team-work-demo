from django.conf.urls.static import static
from django.urls import path

from belbin import settings
from core.views import *



urlpatterns = [
    path(route='', name='index', view=FormView.as_view()),
    path('join-group/', join_group, name='join_group'),
]

# https://github.com/fabiocaccamo/django-admin-interface/issues/4
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)