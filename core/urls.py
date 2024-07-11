from django.conf.urls.static import static
from django.urls import path

from belbin import settings
from core.views import JoinGroupView, GroupListView, GroupDetailView

urlpatterns = [
    path(route='group/', view=GroupListView.as_view(), name='groups_list'),
    path(route='join/<str:name>', view=JoinGroupView.as_view(), name='join_group'),
    path(route='group/<int:pk>/', view=GroupDetailView.as_view(), name='group_detail'),
]

# https://github.com/fabiocaccamo/django-admin-interface/issues/4
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)