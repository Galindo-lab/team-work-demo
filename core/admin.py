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
    model = GroupForm
    #readonly_fields = ('user', 'result', "done")
    extra = 0

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return fields[::-1]  # Invierte el orden de los campos



@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupFormInline]
    # filter_horizontal = ('members',)


#admin.site.register(BelbinProfile)