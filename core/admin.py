from django.contrib import admin
from .models import *


# Register your models here.

class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


@admin.register(EvaluationForm)
class EvaluationFormAdmin(admin.ModelAdmin):
    exclude = ('section',)
    inlines = [SectionInline]

