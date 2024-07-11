from django.conf.urls.static import static
from django.urls import path

from belbin import settings
from core.views import JoinGroupView, GroupListView

urlpatterns = [
    path(route='groups/', view=GroupListView.as_view(), name='groups'),
    path(route='join/<str:name>', view=JoinGroupView.as_view(), name='join_group'),
]

# https://github.com/fabiocaccamo/django-admin-interface/issues/4
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)