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
    readonly_fields = ('title',)
    extra = 0


@admin.register(EvaluationForm)
class EvaluationFormAdmin(admin.ModelAdmin):
    exclude = ('section',)
    inlines = [SectionInline]


class GroupFormInline(admin.TabularInline):
    model = EvaluationResult
    extra = 0

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return fields[::-1]  # Invierte el orden de los campos

    # Método para hacer los campos readonly
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Esto significa que el objeto ya existe (no es nuevo)
            return [field.name for field in self.model._meta.fields]
        return []

    # Método para evitar la edición de inlines
    def has_change_permission(self, request, obj=None):
        if obj:  # Esto significa que el objeto ya existe (no es nuevo)
            return False
        return True




@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupFormInline]
    # filter_horizontal = ('members',)


#admin.site.register(BelbinProfile)