from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BelbinRole(models.TextChoices):
    """
    Define los posibles roles Belbin en el sistema.
    """
    RESOURCE_INVESTIGATOR = 'RI', _("Resource Investigator")
    TEAM_WORKER = 'TW', _("Team Worker")
    COORDINATOR = 'CO', _("Coordinator")
    PLANT = 'PL', _("Plant")
    MONITOR_EVALUATOR = 'ME', _("Monitor Evaluator")
    SPECIALIST = 'SP', _("Specialist")
    SHAPER = 'SH', _("Shaper")
    IMPLEMENTER = 'IM', _("Implementer")
    COMPLETER_FINISHER = 'CF', _("Completer Finisher")


class BelbinProfile(models.Model):
    # perfiles de belbin
    resource_investigator = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    team_worker = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    coordinator = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    plant = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    monitor_evaluator = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    specialist = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    shaper = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    implementer = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    completer_finisher = models.IntegerField(default=0, validators=[MinValueValidator(0)])


class EvaluationForm(models.Model):
    title = models.CharField(max_length=250, default="a")
    section = models.ManyToManyField(to='Question', related_name='fsfdsfsd')

    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=250)
    evaluation = models.ForeignKey(EvaluationForm, on_delete=models.CASCADE, related_name='sections')
    questions = models.ManyToManyField(to='Question', related_name='sections', blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=250)
    profile = models.CharField(choices=BelbinRole.choices, max_length=2)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='qewq')

    def __str__(self):
        return self.title
