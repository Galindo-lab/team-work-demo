from django.contrib import admin
from .models import *


# Register your models here.


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    exclude = ('questions', 'evaluation')


class SectionInline(admin.StackedInline):
    model = Section
    show_change_link = True
    exclude = ('questions',)
    extra = 0


@admin.register(EvaluationForm)
class EvaluationFormAdmin(admin.ModelAdmin):
    exclude = ('section',)
    inlines = [SectionInline]
