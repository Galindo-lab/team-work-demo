from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator


class Profile(models.Model):
    """
    Esta clase permite agregar informacion adicional de los usuarios
    permite extender los perfiles sin modificar User
    """

    # TODO: agregar un campo que represente el perfil global
    # TODO: agregar un campo para representar la opinion de los demas repecto a ti

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)


class Group(models.Model):
    """
    Modelo para representar un grupo al que se puede integrar un miembro
    """
    name = models.CharField(
        max_length=200)

    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='administered_groups')

    class Meta:
        # permite que haya nombre repetidos mientras el administrador
        # no sea el mismo

        unique_together = (('name', 'admin'))


class Member(models.Model):
    """
    Relaciona los miembros con los grupos 
    """

    member = models.ForeignKey(
        User,
        related_name='group_member',
        on_delete=models.CASCADE)

    group = models.ForeignKey(
        Group,
        related_name='members',
        on_delete=models.CASCADE)

    class Meta:
        unique_together = (('member', 'group'))

    def profiles(self):
        profiles = ProfileForm.objects.filter(
            member=self)

        if not profiles.exists():
            return []

        return profiles.first().primary_roles()


class BelbinProfile(models.Model):
    class Roles(Enum):
        RESOURCE_INVESTIGATOR = 'resource_investigator'
        TEAM_WORKER = 'team_worker'
        COORDINATOR = 'coordinator'
        PLANT = 'plant'
        MONITOR_EVALUATOR = 'monitor_evaluator'
        SPECIALIST = 'specialist'
        SHAPER = 'shaper'
        IMPLEMENTER = 'implementer'
        COMPLETER_FINISHER = 'completer_finisher'

    # perfiles de belbin
    resource_investigator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    team_worker = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    coordinator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    plant = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    monitor_evaluator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    specialist = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    shaper = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    implementer = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    completer_finisher = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)])

    def primary_roles(self):
        """Retorna la lista de los perfiles mas altos

        Returns:
            list: lista con los perfiles
        """

        max_value = max(
            self.resource_investigator,
            self.team_worker,
            self.coordinator,
            self.plant,
            self.monitor_evaluator,
            self.specialist,
            self.shaper,
            self.implementer,
            self.completer_finisher,
        )

        # lista con los nombres de los perfiles más altos
        a = self.to_dict()

        b = [k for k in a if a[k] == max_value]

        return b

    def to_dict(self):
        """extrae los valores de cada perfil y los retona como un diccionario

        Returns:
            dict: resultado para cada perfil
        """
        return {
            "resource_investigator": self.resource_investigator,
            "team_worker": self.team_worker,
            "coordinator": self.coordinator,
            "plant": self.plant,
            "monitor_evaluator": self.monitor_evaluator,
            "specialist": self.specialist,
            "shaper": self.shaper,
            "implementer": self.implementer,
            "completer_finisher": self.completer_finisher,
        }


class ProfileForm(BelbinProfile):
    """
    formularios realizados
    """

    # datos del usuario
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    # metadatos de la calse

    class Meta:
        ordering = ['-timestamp']
