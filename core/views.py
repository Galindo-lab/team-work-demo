from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BelbinForm
from .models import BelbinProfile


class FormView(CreateView):
    model = BelbinProfile
    form_class = BelbinForm
    template_name = 'belbin.html'
    success_url = reverse_lazy('yourmodel-list')
