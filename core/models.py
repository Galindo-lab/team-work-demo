# models.py
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
import json

class BelbinRole(models.TextChoices):
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
    class Meta:
        abstract = True

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
    title = models.TextField()
    sinopsis = models.TextField()
    instructions = models.TextField()
    section = models.ManyToManyField(to='Question', related_name='fsfdsfsd')

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'sinopsis': self.sinopsis,
            'instructions': self.instructions,
            'sections': [section.to_dict() for section in self.sections.all()]
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class Section(models.Model):
    title = models.TextField()
    evaluation = models.ForeignKey(EvaluationForm, on_delete=models.CASCADE, related_name='sections')
    questions = models.ManyToManyField(to='Question', related_name='sections', blank=True)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'questions': [question.to_dict() for question in Question.objects.filter(section=self)],
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class Question(models.Model):
    title = models.TextField()
    profile = models.CharField(choices=BelbinRole.choices, max_length=2)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='qewq')

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'profile': self.profile
        }


class EvaluationResult(BelbinProfile):
    group = models.ForeignKey(to='Group', on_delete=models.CASCADE, related_name='groups')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)


class Group(models.Model):
    class Meta():
        unique_together = ('name', 'creator')

    name = models.CharField(max_length=250)
    evaluation = models.ForeignKey(to=EvaluationForm, on_delete=models.CASCADE)
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    code = models.CharField(max_length=25)
    members = models.ManyToManyField(to=User, through=EvaluationResult, related_name='qweqeff')

    def __str__(self):
        return self.name
