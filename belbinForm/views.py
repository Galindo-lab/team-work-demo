from django.shortcuts import render

# Create your views here.
from django.http import (HttpResponse, HttpResponseRedirect)

from belbinForm.models import *
from .forms import BelbinQuestionaryForm


def form(request):
    if request.method != 'POST':
        # enviar el formulario vacio
        return render(request, 'belbinForm.html',
                      {'form': BelbinQuestionaryForm()})

    # si el formulario no esta vacio recuperar los datos
    form = BelbinQuestionaryForm(request.POST)

    
    if not form.is_valid():
        return HttpResponse("Formulario invalido")

    
    questionary = BelbinQuestionary()

    section_1 = BelbinSection(
        questionary=questionary,
        **form.get_section_1()
    )

    # almacenart los datos en la base de datos
    questionary.save()
    section_1.save()

    return HttpResponse("%s." % str(form.get_section_1()))
