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
    resource_investigator = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    team_worker = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    coordinator = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    plant = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    monitor_evaluator = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    specialist = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    shaper = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    implementer = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    completer_finisher = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
