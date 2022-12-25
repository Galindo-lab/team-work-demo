from django.contrib import admin

# Register your models here.
from .models import (BelbinQuestionary, BelbinSection)


class BelbinQuestionaryAdmin(admin.ModelAdmin):
    """
    Hace visibles los campos no editables en el administrador
    - fuente: https://stackoverflow.com/a/23660030
    """
    readonly_fields = (
        'creation_datetime',
    )

admin.site.register(BelbinQuestionary,BelbinQuestionaryAdmin)
admin.site.register(BelbinSection)
