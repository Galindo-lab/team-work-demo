from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator

import json


class Profile(models.Model):
    """
    Esta clase permite agregar informacion adicional de los usuarios
    permite extender los perfiles sin modificar User
    """

    # TODO: agregar un campo que represente el perfil global

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Group(models.Model):
    """
    Modelo para representar un grupo al que se puede integrar un miembro
    """
    name = models.CharField(
        max_length=200
    )

    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_admin'
    )

    class Meta:
        # permite que haya nombre repetidos mientras el administrador
        # no sea el mismo

        unique_together = (
            ('name', 'admin'),
        )


class Member(models.Model):
    """
    Relaciona los miembros con los grupos 
    """

    member = models.ForeignKey(
        User,
        related_name='group_member',
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        Group,
        related_name='members',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            ('member', 'group'),
        )

    def profiles(self):
        profiles = BelbinUserProfile.objects.filter(
            member=self
        )

        if not profiles.exists():
            return []

        return profiles.first().results()


class BelbinUserProfile(models.Model):
    """
    formularios realizados
    """

    # datos del usuario
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    # perfiles de belbin
    resource_investigator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    team_worker = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    coordinator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    plant = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    monitor_evaluator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    specialist = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    shaper = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    implementer = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    
    completer_finisher = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    # metadatos de la calse
    class Meta:
        ordering = ['-timestamp']

    def results(self):
        """Retorna la lista de los perfiles mas altos

        Returns:
            list: lista con los perfiles
        """

        max_value = max([
            self.resource_investigator,
            self.team_worker,
            self.coordinator,
            self.plant,
            self.monitor_evaluator,
            self.specialist,
            self.shaper,
            self.implementer,
            self.completer_finisher,
        ])

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

    def json_profiles(self):
        """retorna los datos en forma de json

        Returns:
            string: json de los puntos que dan los perfiles 
        """
        return json.dumps(self.to_dict())
