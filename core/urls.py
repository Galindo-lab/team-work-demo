from django.conf.urls.static import static
from django.urls import path

from belbin import settings
from core.views import JoinGroupView
from core.views import GroupListView
from core.views import GroupDetailView
from core.views import AnswerFormView

urlpatterns = [
    path(route='group/', view=GroupListView.as_view(), name='groups_list'),
    path(route='join/<int:pk>', view=JoinGroupView.as_view(), name='join_group'),
    path(route='group/<int:pk>/', view=GroupDetailView.as_view(), name='group_detail'),
    path(route='form/<int:pk>/', view=AnswerFormView.as_view(), name='form'),
]

# https://github.com/fabiocaccamo/django-admin-interface/issues/4
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)